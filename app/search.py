from whoosh.index import create_in, exists_in, open_dir
from whoosh.qparser import MultifieldParser

from models import Document, Corpus


def get_or_create_index(path, schema, src):
    """Get or create an Index."""
    index = open_dir(path) if exists_in(path) else create_in(path, schema)
    indexed_titles = set(field['title'] for field in gen_indexed_fields(index))
    corpus = Corpus(src)
    documents = set(corpus.gen_documents())
    update_index(index.writer(), indexed_titles, documents)
    return index


def gen_indexed_fields(index):
    with index.searcher() as searcher:
        for field in searcher.all_stored_fields():
            yield field


def update_index(writer, indexed_titles, documents):
    for document in documents:
        if document.title not in indexed_titles:
            writer.add_document(title=document.title, content=document.content,
                                time=document.time)
        elif document.is_stale:
            writer.delete_by_term('title', document.title)
            writer.add_document(title=document.title, content=document.content,
                                time=document.time)

    document_titles = set(document.title for document in documents)
    for title in indexed_titles - document_titles:
        writer.delete_by_term('title', title)
    writer.commit()


def gen_results(index, q):
    with index.searcher(closereader=False) as searcher:
        results = searcher.search(q)
        for result in results:
            yield Document(result['title'], result['time'])


def search(index, querystring):
    q = MultifieldParser(["title", "content"], index.schema).parse(querystring)
    return gen_results(index, q)
