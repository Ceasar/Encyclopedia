import os

from flask import redirect, render_template, request, url_for
import jinja2

from models import SCHEMA
from rst import iteritems, get_hyperlink_target
import search

INDEX = "config/index.rst"
INDEX_PATH = '.index'
SRC = "src"


def index():
    reference_names = [k for k, _ in iteritems(INDEX)]
    return render_template("_layouts/index.html", anchors=reference_names)


def article(name):
    if name.endswith(".html"):
        return redirect(url_for("article", name=name.replace(".html", "")))
    try:
        return render_template(name + ".html")
    except jinja2.exceptions.TemplateNotFound:
        index = dict(iteritems(INDEX))
        reference_name = name.replace("_", " ")
        return redirect(get_hyperlink_target(index, reference_name))


def search_view():
    if not os.path.isdir(INDEX_PATH):
        os.mkdir(INDEX_PATH)
    search_index = search.get_or_create_index(INDEX_PATH, SCHEMA, SRC)
    querystring = request.args.get('q')
    results = list(search.search(search_index, querystring))

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
