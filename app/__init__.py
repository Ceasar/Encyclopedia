from flask import Flask

from models import Corpus
from views import index, article, open_search, search_view

from settings import SRC


def create_app():
    app = Flask(__name__)
    app.corpus = Corpus(SRC)
    app.route("/")(index)
    app.route("/<name>")(article)
    app.route("/opensearch")(open_search)
    app.route("/search")(search_view)
    return app
