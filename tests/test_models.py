import datetime

from app.models import Document


def test_title():
    doc = Document("src/Andy_Warhol.rst")
    assert doc.title == "src/Andy_Warhol.rst"


def test_datetime():
    doc = Document("Test", time=1411320556.0)
    assert doc.datetime == datetime.datetime(2014, 9, 21, 10, 29, 16)


def test_filename():
    doc = Document("src/Andy_Warhol.rst")
    assert doc.filename == "Andy_Warhol"


def test_contents(tmpdir):
    p = tmpdir.join("Andy_Warhol.rst")
    content = (
    """
    ***********
    Andy Warhol
    ***********

    **Andy Warhol** was an artist.
    """)
    p.write(content)
    assert Document(p).content == content


def test_html(tmpdir):
    p = tmpdir.join("Andy_Warhol.rst")
    content = ("***********\n"
               "Andy Warhol\n"
               "***********\n"
               "**Andy Warhol** was an artist.")
    p.write(content)
    doc = Document(p)
    html = doc.html
    assert '<h1 class="title">Andy Warhol</h1>' in html
    assert '<p><strong>Andy Warhol</strong> was an artist.</p>' in html
