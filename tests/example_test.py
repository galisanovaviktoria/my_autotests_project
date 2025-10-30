import os

def test_guest_can_open_homepage(browser):
    base_url = os.getenv("BASE_URL", "https://example.com")
    browser.get(base_url)
    assert "Example Domain" in browser.title
