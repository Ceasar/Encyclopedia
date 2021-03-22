import collections
import os

from algoliasearch.search_client import SearchClient

from models import Corpus
from rst import get_references
from settings import SRC


Card = collections.namedtuple('Card', ['id', 'document', 'keywords', 'text'])


def get_paragraph_links(paragraph):
    return get_references(paragraph)


def _gen_paragraphs(corpus):
    for document in corpus.gen_documents():
        for paragraph in document.gen_paragraphs():
            yield document.filename, paragraph.replace('\n', ' ')


def gen_cards(corpus):
    for title, paragraph in _gen_paragraphs(corpus):
        pid = hash(paragraph)
        keywords = get_paragraph_links(paragraph)
        card = Card(pid, title, keywords, paragraph)
        yield card


def save_cards_to_search_index(algolia_app_id, algolia_api_key, algolia_index_name='cards'):
    client = SearchClient.create(algolia_app_id, )
    index = client.init_index(algolia_index_name)

    corpus = Corpus(SRC)
    cards = [
        {
            'id': card.id,
            'document': card.document,
            'keywords': card.keywords,
            'text': card.text
        }
        for card in gen_cards(corpus)
    ]
    batch = cards
    index.save_objects(batch, {'autoGenerateObjectIDIfNotExist': True})
    index.set_settings({"searchableAttributes": ['keywords', 'text']})


def main():
    import os
    save_cards_to_search_index(
        os.environ['ALGOLIA_APP_ID'],
        os.environ['ALGOLIA_API_KEY'],
    )


if __name__ == '__main__':
    main()
