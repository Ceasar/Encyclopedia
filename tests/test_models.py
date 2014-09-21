import datetime

from app.models import Document


def test_title():
    doc = Document("Test")
    assert doc.title == "Test"


def test_datetime():
    doc = Document("Test", time=1411320556.0)
    assert doc.datetime == datetime.datetime(2014, 9, 21, 10, 29, 16)
