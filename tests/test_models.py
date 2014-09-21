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
