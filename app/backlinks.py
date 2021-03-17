import collections
import json

import docutils.nodes
import docutils.parsers.rst
import docutils.utils
import docutils.frontend

from models import Corpus
from rst import iteritems, get_hyperlink_target
from settings import  INDEX


DICT = dict(iteritems(INDEX))


def get_canonical_name(name):
    reference_name = name.replace("_", " ")
    return get_hyperlink_target(DICT, reference_name)


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


def get_out_links():
    corpus = Corpus('src')
    links = {}
    for doc in corpus.gen_documents():
        text = doc.content
        try:
            refs = get_references(text)
        except:
            continue
        else:
            # print(doc.filename, refs)
            out_links = []
            for ref in set(refs):
                try:
                    canonical_name = get_canonical_name(ref)
                    while not canonical_name.endswith('html'):
                        canonical_name = get_canonical_name(canonical_name)
                except KeyError:
                    # print('KeyError:', doc.title, ref)
                    pass
                else:
                    out_links.append(canonical_name)
            links[doc.filename] = set(out_links)
    return links


def invert_dict(dict_):
    inverted = collections.defaultdict(list)
    for key, values in dict_.items():
        for value in values:
            inverted[value].append(key)
    return dict(inverted)


def get_inverted_index():
    out_links = get_out_links()
    return invert_dict(out_links)


def main():
    inverted_index = get_inverted_index()
    print(json.dumps(inverted_index, indent=4, sort_keys=True))

main()
