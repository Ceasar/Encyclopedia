from app.models import Document


def test_title():
    doc = Document("Test")
    assert doc.title == "Test"
