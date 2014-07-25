from flask import Flask

from views import index, article, search


def create_app():
    app = Flask(__name__)
    app.route("/")(index)
    app.route("/<name>")(article)
    app.route("/search")(search)
    return app
