import os
import os.path

from flask import Flask, redirect, render_template, request, url_for
import jinja2

app = Flask(__name__)

INDEX = "config/index.rst"


def iteritems(filename):
    with open(filename) as f:
        for line in f:
            reference_name, hyperlink_target = line.split(":")
            # strip the leading ".. _" from the reference_name
            reference_name = reference_name[4:]
            yield reference_name, hyperlink_target.strip()


def get_hyperlink_target(index, reference_name):
    hyperlink_target = index[reference_name]
    if hyperlink_target.endswith("_"):
        while hyperlink_target.endswith("_"):
            reference_name = hyperlink_target[:-1].replace("`", "")
            hyperlink_target = index[reference_name]
        return os.path.splitext(hyperlink_target)[0]
    else:
        return hyperlink_target


@app.route("/")
def index():
    reference_names = [k for k, _ in iteritems(INDEX)]
    return render_template("_layouts/index.html", anchors=reference_names)


@app.route("/<name>")
def article(name):
    if name.endswith(".html"):
        return redirect(url_for("article", name=name.replace(".html", "")))
    try:
        return render_template(name + ".html")
    except jinja2.exceptions.TemplateNotFound:
        index = dict(iteritems(INDEX))
        reference_name = name.replace("_", " ")
        return redirect(get_hyperlink_target(index, reference_name))


@app.route("/search")
def search():
    name = request.args['q'].replace(" ", "_")
    return redirect(url_for("article", name=name))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
