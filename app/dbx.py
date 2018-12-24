from rst import iteritems, rst_to_html


class Document(object):
    def __init__(self, title, content):
        self._title = title
        self._content = content

    def html(self, index, directive_file):
        content = ''.join([index.rst, directive_file.rst, self._content])
        return rst_to_html(content)


class Corpus(object):
    def __init__(self, dbx):
        self._dbx = dbx

    def find(self, name):
        _, resp = self._dbx.files_download('/documents/{}.rst'.format(name))
        return Document(name, resp.text)

    def find_image(self, name):
        path = '/images/{}'.format(name)
        metadata, resp = self._dbx.files_download(path)
        return resp.content


class Index(object):
    def __init__(self, dbx):
        self._dbx = dbx

    def keys(self):
        metadata, resp = self._dbx.files_download('/config/index.rst')
        lines = resp.text.split('\n')
        items = [k for (k, _) in iteritems(lines)]
        print items[0], items[-1], len(items)
        return items

    @property
    def rst(self):
        _, resp = self._dbx.files_download('/config/index.rst')
        return resp.text


class DirectiveFile(object):
    def __init__(self, dbx):
        self._dbx = dbx

    @property
    def rst(self):
        _, resp = self._dbx.files_download('/config/directives.rst')
        return resp.text
