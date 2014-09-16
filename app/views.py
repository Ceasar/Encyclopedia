import os

from flask import abort, redirect, render_template, request, url_for

from models import SCHEMA, Document
from rst import iteritems, get_hyperlink_target
import search
from settings import INDEX, INDEX_PATH, SRC


def index():
    reference_names = [k for k, _ in iteritems(INDEX)]
    return render_template("_layouts/index.html", anchors=reference_names)


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
            rst_filename = os.path.join(SRC, name + ".rst")
            document = Document(rst_filename)
            return document.html
        except IOError:
            index = dict(iteritems(INDEX))
            reference_name = name.replace("_", " ")
            try:
                target = get_hyperlink_target(index, reference_name)
            except KeyError:
                abort(404)
            else:
                return redirect(target)


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
