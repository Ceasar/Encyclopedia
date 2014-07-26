import datetime
import os
import unicodedata

from whoosh.fields import Schema, ID, KEYWORD, STORED, TEXT

SCHEMA = Schema(
    content=TEXT(stored=True),
    tags=KEYWORD,
    title=ID(unique=True, stored=True),
    time=STORED,
)


class Document(object):
    """
    A document consist of body or block-level elements, and may be structured
    into sections.

    """
    def __init__(self, title, time, tags=None):
        self._title = title
        self.time = time
        self.tags = tags or []

    @property
    def content(self):
        with open(self.title, 'rU') as f:
            return unicode(self._decode(f.read()))

    @property
    def datetime(self):
        return datetime.datetime.fromtimestamp(self.time)

    @property
    def filename(self):
        return os.path.splitext(os.path.split(self.title)[-1])[0]

    def gen_elements(self):
        line_buffer = []
        with open(self.title, 'rU') as f:
            for line in f:
                if line.strip():
                    line_buffer.append(line.rstrip())
                else:
                    if line_buffer:
                        yield self._decode("\n".join(line_buffer))
                    line_buffer = []
        if line_buffer:
            yield self._decode("\n".join(line_buffer))

    def gen_paragraphs(self):
        for element in self.gen_elements():
            if self._element_is_paragraph(element):
                yield element

    @property
    def is_stale(self):
        return os.path.getmtime(self.title) > self.time

    @property
    def paragraphs(self):
        return list(self.gen_paragraphs())

    @property
    def reference_name(self):
        return self.filename.replace("_", " ")

    @property
    def title(self):
        return unicode(self._title)

    def _element_is_section_title(self, element):
        lines = element.split('\n')
        return any(len(set(line)) == 1 for line in lines)

    def _element_is_paragraph(self, element):
        if self._element_is_section_title(element):
            return False
        else:
            return element[0].isalpha() or element[0] == "*"

    def _decode(self, text, encoding="UTF-8"):
        """
        Encode a Unicode string as ascii, ignoring any errors.
        """
        unistr = text.decode(encoding)
        form = unicodedata.normalize('NFKD', unistr)
        return form.encode('ascii', 'ignore')


def gen_documents(src):
    for dirpath, _, filenames in os.walk(src):
        for filename in filenames:
            if not filename.startswith("."):
                filepath = os.path.join(dirpath, filename)
                modtime = os.path.getmtime(filepath)
                yield Document(title=filepath, time=modtime)
