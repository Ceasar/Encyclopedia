import os
import os.path

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


def get_index():
    index = {}
    with open("src/index") as f:
        for line in f:
            anchor, target = line.split(":")
            index[anchor[4:].title()] = target.strip()
    return index


@app.route("/")
def index():
    anchors = get_index().keys()
    return render_template("_layouts/index.html", anchors=anchors)


@app.route("/<name>")
def article(name):
    if name.endswith(".html"):
        return redirect(url_for("article", name=name.replace(".html", "")))
    index = get_index()
    anchor = name.replace("_", " ").title()
    target = index[anchor]
    if target.endswith("_"):
        while target.endswith("_"):
            anchor = target[:-1].replace("`", "").title()
            target = index[anchor]
        name = os.path.splitext(target)[0]
        return redirect(url_for("article", name=name))
    else:
        return render_template(target)


@app.route("/search")
def search():
    name = request.args['q'].replace(" ", "_")
    return redirect(url_for("article", name=name))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
