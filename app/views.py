from flask import redirect, render_template, request, url_for
import jinja2

from rst import iteritems, get_hyperlink_target

INDEX = "config/index.rst"


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


def search():
    name = request.args['q'].replace(" ", "_")
    return redirect(url_for("article", name=name))
