import io
import os

from flask import (abort, current_app, redirect, render_template, request,
                   url_for, send_file, jsonify)


def index():
    reference_names = current_app.index.keys()
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
            document = current_app.corpus.find(name)
        except ValueError:
            try:
                canonical_name = current_app.corpus.get_canonical_name(name)
            except KeyError:
                abort(404)
            else:
                return redirect(canonical_name)
        else:
            return document.html(current_app.index, current_app.directive_file)


def view_image(name):
    content = current_app.corpus.find_image(name)
    filename, ext = os.path.splitext(name)
    mimetype = 'image/svg+xml' if ext == '.svg' else 'image/{}'.format(ext[1:])
    return send_file(
        io.BytesIO(content),
        mimetype=mimetype,
    )


def search_result():
    querystring = request.args.get('q')
    search_result = current_app.dbx.files_search('/documents', querystring)
    # Note that searching file content is only available for Dropbox Business
    # accounts.
    return jsonify({
        'matches': [
            {
                'name': match.metadata.name,
                'path_display': match.metadata.path_display,
                'path_lower': match.metadata.path_lower,
                'filename': match.match_type.is_filename(),
                'content': match.match_type.is_content(),
            } for match in search_result.matches
        ],
        'more': search_result.more
    })
