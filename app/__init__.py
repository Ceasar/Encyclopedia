import dropbox
from flask import Flask

from dbx import Corpus, DirectiveFile, Index
from views import index, article, search_result, view_image


def create_app(access_token):
    app = Flask(__name__)

    dbx = dropbox.Dropbox(access_token)
    app.dbx = dbx
    app.corpus = Corpus(dbx)
    app.index = Index(dbx)
    app.directive_file = DirectiveFile(dbx)

    app.route("/")(index)
    app.route("/images/<name>")(view_image)
    app.route("/search")(search_result)
    app.route("/<name>")(article)
    return app
