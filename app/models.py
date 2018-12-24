from whoosh.fields import Schema, ID, KEYWORD, STORED, TEXT

SCHEMA = Schema(
    content=TEXT(stored=True),
    tags=KEYWORD,
    title=ID(unique=True, stored=True),
    time=STORED,
)
