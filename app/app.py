from flask import Flask

from app.models import Corpus
from app.settings import SRC
from app.views import index, article, open_search


def create_app():
    app = Flask(__name__)
    app.corpus = Corpus(SRC)
    app.route("/")(index)
    app.route("/<name>")(article)
    app.route("/opensearch")(open_search)
    return app
