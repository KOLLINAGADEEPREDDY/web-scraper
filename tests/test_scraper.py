from scraper.main import fetch_title

def test_example():
    assert 2 + 2 == 4

def test_fetch_title():
    url = "https://example.com"
    assert "Example Domain" in fetch_title(url)

    # In test/test_main.py
def test_math():
    assert 1 + 1 == 2