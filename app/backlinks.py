import collections
import json

from models import Corpus
from rst import iteritems, get_hyperlink_target, get_references
from settings import  INDEX


DICT = dict(iteritems(INDEX))


def get_canonical_name(name):
    reference_name = name.replace("_", " ")
    return get_hyperlink_target(DICT, reference_name)


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
