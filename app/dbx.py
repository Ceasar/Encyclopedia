from collections import namedtuple
import os

import dropbox

from rst import iteritems


Image = namedtuple('Image', ['content_type', 'content'])


class DropboxClient(object):
    def __init__(self, dbx):
        self._dbx = dbx

    def get_canonical_name(self, name):
        index = dict(iteritems(self.get_index().split('\n')))
        key = name.lower()
        while True:
            try:
                key = index[key]
            except KeyError:
                break
            else:
                if key.endswith('_'):
                    key = key[:-1]
        filename, _ = os.path.splitext(key)
        return filename

    def get_document(self, name):
        try:
            _, resp = self._dbx.files_download('/documents/{}.rst'.format(name))
        except dropbox.exceptions.ApiError:
            raise ValueError('No file named: "{}"'.format(name))
        else:
            return ''.join([self.get_index(), self.get_directives(), resp.text])

    def get_directives(self):
        _, resp = self._dbx.files_download('/config/directives.rst')
        return resp.text

    def get_image(self, name):
        path = '/images/{}'.format(name)
        metadata, resp = self._dbx.files_download(path)

        filename, ext = os.path.splitext(name)
        content_type = ('image/svg+xml' if ext == '.svg' else
                        'image/{}'.format(ext[1:]))

        return Image(content_type, resp.content)

    def get_index(self):
        _, resp = self._dbx.files_download('/config/index.rst')
        return resp.text

    def get_index_keys(self):
        lines = self.get_index().split('\n')
        items = [k for (k, _) in iteritems(lines)]
        return items

    def search_files(self, querystring):
        search_result = self._dbx.files_search('/documents', querystring)
        # Note that searching file content is only available for Dropbox
        # Business accounts.
        return [
            self._parse_search_result(match) for match in search_result.matches
        ]

    def _parse_search_result(self, match):
        filename, ext = os.path.splitext(match.metadata.name)
        return {
            'filename': filename,
            'reference_name': filename.replace('_', ' '),
        }
