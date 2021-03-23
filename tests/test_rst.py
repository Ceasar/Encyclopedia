from app.rst import parse_elements


PARAGRAPHS = (
"""
Paragraph 1

Paragraph 2
"""
)

UNORDERED_LIST = (
"""
Fruits:

- Apple
- Orange

Paragraph 2
"""
)

ORDERED_LIST = (
"""
Fruits:

1. Apple
2. Orange

Paragraph 2
"""
)

CODE_BLOCK = (
"""
Code:

    x = 1

Paragraph 2
"""
)


QUOTE = (
"""
Quote:

    Early to rise, early to bed.

    -- Ben Franklin

Paragraph 2
"""
)


def test_parse_paragraphs():
    lines = PARAGRAPHS.strip().split('\n')
    elements = list(parse_elements(lines))
    assert elements == ['Paragraph 1', 'Paragraph 2']


def test_parse_unordered_list():
    lines = UNORDERED_LIST.strip().split('\n')
    elements = list(parse_elements(lines))
    assert elements == ['Fruits:\n\n- Apple\n- Orange', 'Paragraph 2']


def test_parse_ordered_list():
    lines = ORDERED_LIST.strip().split('\n')
    elements = list(parse_elements(lines))
    assert elements == ['Fruits:\n\n1. Apple\n2. Orange', 'Paragraph 2']


def test_parse_code_block():
    lines = CODE_BLOCK.strip().split('\n')
    elements = list(parse_elements(lines))
    assert elements == ['Code:\n\n    x = 1', 'Paragraph 2']


def test_parse_quote():
    lines = QUOTE.strip().split('\n')
    elements = list(parse_elements(lines))
    assert elements == [
        'Quote:\n\n    Early to rise, early to bed.\n\n    -- Ben Franklin',
        'Paragraph 2'
    ]
