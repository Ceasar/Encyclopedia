"""
Utility functions for working with reStructuredText.
"""
import os
import os.path

from docutils import core
import docutils.nodes
import docutils.parsers.rst
import docutils.utils
import docutils.frontend
from docutils.writers.html4css1 import Writer, HTMLTranslator


def iteritems(filename):
    with open(filename) as f:
        for line in f:
            try:
                reference_name, hyperlink_target = line.split(":")
            except ValueError:
                # the line has multiple ":" in it; probably an external link
                continue
            # strip the leading ".. _" from the reference_name
            reference_name = reference_name[4:]
            yield reference_name.lower(), hyperlink_target.strip()


def get_hyperlink_target(index, reference_name):
    hyperlink_target = index[reference_name.lower()]
    if hyperlink_target.endswith("_"):
        while hyperlink_target.endswith("_"):
            reference_name = hyperlink_target[:-1].replace("`", "")
            hyperlink_target = index[reference_name.lower()]
        return os.path.splitext(hyperlink_target)[0]
    else:
        return hyperlink_target


SETTINGS = {
    # Include a time/datestamp in the document footer.
    'datestamp': '%Y-%m-%d %H:%M UTC',
    # Output math blocks as LaTeX that can be interpreted by MathJax for
    # a prettier display of Math formulas.
    'math_output': 'MathJax',
    # Recognize and link to standalone PEP references (like "PEP 258").
    'pep_references': 1,
    # Do not report any system messages.
    'report_level': 5,
    # Recognize and link to standalone RFC references (like "RFC 822").
    'rfc_references': 1,
}


def rst_to_html(rst_string, settings=None):
    """Convert a string written in reStructuredText to an HTML string.

    :param rst_string:
        A string that holds the contents of a reStructuredText document.

    :param settings:
        Optional. A dictionary which overrides the default settings.

        For a list of the possible keys and values, see
        http://docutils.sourceforge.net/docs/user/config.html.

        To log the values used, pass in ``'dump_settings': 'yes'``.
    """
    writer = Writer()
    writer.translator_class = HTMLTranslator
    if settings is None:
        document = core.publish_string(rst_string, writer=writer,
                                       settings_overrides=SETTINGS)
    return str(document, "utf-8")


def rst_to_html_fragment(text):
    parts = core.publish_parts(source=text,
                              writer_name='html',
                              settings_overrides=SETTINGS)
    return parts['body_pre_docinfo']+parts['fragment']


class ReferenceVisitor(docutils.nodes.NodeVisitor):
    def __init__(self, doc):
        super().__init__(doc)
        self._references = []

    @property
    def references(self):
        return self._references

    def visit_reference(self, node: docutils.nodes.reference) -> None:
        """Called for "reference" nodes."""
        self._references.append(node)

    def unknown_visit(self, node: docutils.nodes.Node) -> None:
        """Called for all other node types."""
        # print(node)
        pass


def parse_rst(text: str) -> docutils.nodes.document:
    parser = docutils.parsers.rst.Parser()
    components = (docutils.parsers.rst.Parser,)
    settings = docutils.frontend.OptionParser(components=components).get_default_values()
    document = docutils.utils.new_document('<rst-doc>', settings=settings)
    parser.parse(text, document)
    return document


def get_references(text):
    doc = parse_rst(text)
    visitor = ReferenceVisitor(doc)
    doc.walk(visitor)
    return [ref.attributes['refname'] for ref in visitor.references if ref.attributes.get('refname')]
