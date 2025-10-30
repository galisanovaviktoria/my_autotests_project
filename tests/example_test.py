def test_guest_can_open_homepage(browser):
    browser.get("https://www.litres.ru")
    assert "Литрес" in browser.title
    print("✅ Главная страница загружена")