import datetime
import os
import unicodedata

from whoosh.fields import Schema, ID, KEYWORD, STORED, TEXT

from settings import DIRECTIVES, INDEX
from rst import iteritems, get_hyperlink_target, rst_to_html

SCHEMA = Schema(
    content=TEXT(stored=True),
    tags=KEYWORD,
    title=ID(unique=True, stored=True),
    time=STORED,
)

unicode = str


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
            return f.read()

    @property
    def datetime(self):
        """The date and time the document was modified."""
        return datetime.datetime.utcfromtimestamp(self.time)

    @property
    def excerpt(self):
        """A short extract from the document."""
        return next(self.gen_paragraphs())

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
        """
        The contents of the document rendered as HTML.
        """
        parts = []
        try:
            with open(INDEX, 'rU') as index:
                parts.append(index.read())
        except IOError:
            pass
        try:
            with open(DIRECTIVES, 'rU') as directives:
                parts.append(directives.read())
        except IOError:
            pass
        parts.append(self.content)
        body = "".join(parts)
        return rst_to_html(body)

    def gen_elements(self):
        line_buffer = []
        with open(self.title, 'rU') as f:
            for line in f:
                if line.strip():
                    line_buffer.append(line.rstrip())
                else:
                    if line_buffer:
                        yield "\n".join(line_buffer)
                    line_buffer = []
        if line_buffer:
            yield "\n".join(line_buffer)

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
    def html_paragraphs(self):
        return list(rst_to_html(p) for p in self.gen_paragraphs())

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

    def __repr__(self):
        return "Document(title=%s, time=%s, tags=%s)" % (self.title, self.time,
                                                         self.tags)


class Corpus(object):
    """A Corpus represents a set of documents."""
    def __init__(self, directory):
        self.directory = directory

    def find(self, name):
        """Try to find a document named *name* in the corpus."""
        filename = name.replace(" ", "_") + ".rst"
        filepath = os.path.join(self.directory, filename)
        if os.path.exists(filepath):
            return Document(filepath)
        else:
            raise ValueError("No Document named '%s' exists" % name)

    def get_canonical_name(self, name):
        """Find the canonical name for *name*."""
        index = dict(iteritems(INDEX))
        reference_name = name.replace("_", " ")
        return get_hyperlink_target(index, reference_name)

    def gen_documents(self):
        """
        Generate the Documents in a directory tree rooted at directory *top* by
        walking the tree top-down (including *top* itself).
        """
        for dirpath, _, filenames in os.walk(self.directory):
            for filename in filenames:
                if not filename.startswith("."):
                    filepath = os.path.join(dirpath, filename)
                    modtime = os.path.getmtime(filepath)
                    yield Document(title=filepath, time=modtime)
