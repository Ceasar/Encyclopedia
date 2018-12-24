import io
import os

from flask import (abort, current_app, redirect, render_template, request,
                   url_for, send_file)

from .rst import rst_to_html


def index():
    reference_names = current_app.dbx_client.get_index_keys()
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
            document = current_app.dbx_client.get_document(name)
        except ValueError:
            try:
                canonical_name = current_app.dbx_client.get_canonical_name(name)
            except KeyError:
                abort(404)
            else:
                return redirect(canonical_name)
        else:
            return rst_to_html(document)


def view_image(name):
    image = current_app.dbx_client.get_image(name)
    return send_file(
        io.BytesIO(image.content),
        mimetype=image.mimetype,
    )


def search_result():
    querystring = request.args.get('q')
    return render_template(
        "_layouts/search.html",
        querystring=querystring,
        results=current_app.dbx_client.search_files(querystring)
    )
