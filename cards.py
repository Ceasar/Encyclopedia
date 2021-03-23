import os

from algoliasearch.search_client import SearchClient

from app.models import Corpus
from app.rst import get_references, get_strong_nodes
from app.settings import SRC


def gen_paragraphs(corpus):
    for document in corpus.gen_documents():
        for paragraph in document.gen_paragraphs():
            yield document.filename, paragraph.replace('\n', ' ')


def make_card_record(title, paragraph):
    pid = hash(paragraph)
    definitions = get_strong_nodes(paragraph)
    keywords = get_references(paragraph)
    return {
        'id': pid,
        'definitions': definitions,
        'document': title,
        'keywords': keywords,
        'text': paragraph
    }


def save_cards_to_search_index(
    algolia_app_id,
    algolia_api_key,
    cards,
    algolia_index_name='cards',
):
    client = SearchClient.create(algolia_app_id, )
    index = client.init_index(algolia_index_name)

    batch = cards
    index.save_objects(batch, {'autoGenerateObjectIDIfNotExist': True})
    index.set_settings({
        "searchableAttributes": ['definitions', 'keywords', 'text']
    })


def gen_cards():
    corpus = Corpus(SRC)
    return (
        make_card_record(title, paragraph)
        for title, paragraph in gen_paragraphs(corpus)
    )


def main():
    import os
    cards = list(gen_cards())
    save_cards_to_search_index(
        os.environ['ALGOLIA_APP_ID'],
        os.environ['ALGOLIA_API_KEY'],
        cards,
    )


if __name__ == '__main__':
    main()
