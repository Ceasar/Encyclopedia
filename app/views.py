import os
import json

from bs4 import BeautifulSoup
from flask import (abort, current_app, redirect, render_template, request,
                   url_for)

from models import SCHEMA
from rst import iteritems, get_hyperlink_target, rst_to_html_fragment
import search
from settings import INDEX, INDEX_PATH, SRC, BACKLINKS


def index():
    suggestions = []
    corpus = current_app.corpus
    for document in corpus.gen_documents():
        try:
            preview = rst_to_html_fragment(document.excerpt)
        except StopIteration:
            preview = None
        suggestions.append({
            "title": document.reference_name,
            "preview": preview,
        })
    return render_template(
        "_layouts/index.html",
        suggestions=suggestions
    )


def article(name):
    """Generate a HTML page for an article.

    :param name:
        The name of the article.
    """
    if name.endswith(".html"):
        root, _ = os.path.splitext(name)
        return redirect(url_for("article", name=root))
    else:
        try:
            document = current_app.corpus.find(name)
        except ValueError:
            try:
                canonical_name = current_app.corpus.get_canonical_name(name)
            except KeyError:
                abort(404)
            else:
                return redirect(canonical_name)
        else:
            html_doc = document.html
            soup = BeautifulSoup(html_doc, 'html.parser')
            body = str(soup.body)
            title = name.replace('_', ' ')
            backlinks = BACKLINKS.get("{}.html".format(document.filename), [])
            return render_template(
                'article.html',
                document=body,
                title=title,
                backlinks=sorted(backlinks),
            )


def search_view():
    if not os.path.isdir(INDEX_PATH):
        os.mkdir(INDEX_PATH)
    search_index = search.get_or_create_index(INDEX_PATH, SCHEMA, SRC)
    querystring = request.args.get('q')
    results = list(search.search(search_index, querystring))

    if request.args.get('follow'):
        # Redirect to article if a direct hit is found in the INDEX
        index = {k.lower(): v for k, v in iteritems(INDEX)}
        for result in results:
            reference_name = str(querystring).lower()
            try:
                target = get_hyperlink_target(index, reference_name)
            except KeyError:
                pass
            else:
                return redirect(target)

    return render_template("_layouts/search.html", querystring=querystring,
                           results=results)


def open_search():
    return render_template("opensearch.xml"), 200, {'Content-Type': 'text/xml'}
