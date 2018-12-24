import dropbox
from flask import Flask

from dbx import DropboxClient
from views import index, article, search_result, view_image


def create_app(access_token):
    app = Flask(__name__)

    dbx = dropbox.Dropbox(access_token)
    app.dbx_client = DropboxClient(dbx)

    app.route("/")(index)
    app.route("/images/<name>")(view_image)
    app.route("/search")(search_result)
    app.route("/<name>")(article)
    return app
