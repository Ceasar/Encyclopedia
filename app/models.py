import datetime
import os
import unicodedata

from whoosh.fields import Schema, ID, KEYWORD, STORED, TEXT

from rst import rst_to_html
from settings import DIRECTIVES, INDEX

SCHEMA = Schema(
    content=TEXT(stored=True),
    tags=KEYWORD,
    title=ID(unique=True, stored=True),
    time=STORED,
)


class Document(object):
    """
    A document consists of body or block-level elements, and may be structured
    into sections.

    :param title:
        A string representing the path to the file, e.g.
        ``"src/Andy_Warhol.rst"``.

    :param time:
        A float representing the time of last modification of *title* as
        measured in numbers of seconds since the last epoch, e.g.
        ``1405237014.0``.

    :param tags:
        A set of strings representing keywords that describe the file.
    """
    def __init__(self, title, time=None, tags=None):
        self._title = title
        self.time = time
        self.tags = tags or []

    @property
    def content(self):
        """
        Read the contents of a document.
        """
        with open(self.title, 'rU') as f:
            return unicode(self._decode(f.read()))

    @property
    def datetime(self):
        """The date and time the document was modified."""
        return datetime.datetime.fromtimestamp(self.time)

    @property
    def filename(self):
        """
        The name of the file.

        >>> d = Document("src/Andy_Warhol.rst")
        >>> d.filename
        'Andy_Warhol'
        """
        return os.path.splitext(os.path.split(self.title)[-1])[0]

    @property
    def html(self):
        with open(INDEX, 'rU') as index, open(DIRECTIVES, 'rU') as directives:
            body = index.read() + directives.read() + self.content
            return rst_to_html(body)

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

    def __repr__(self):
        return "Document(title=%s, time=%s, tags=%s)" % (self.title, self.time,
                                                         self.tags)


def gen_documents(top):
    """
    Generate the Documents in a directory tree rooted at directory *top* by
    walking the tree top-down (including *top* itself).
    """
    for dirpath, _, filenames in os.walk(top):
        for filename in filenames:
            if not filename.startswith("."):
                filepath = os.path.join(dirpath, filename)
                modtime = os.path.getmtime(filepath)
                yield Document(title=filepath, time=modtime)
