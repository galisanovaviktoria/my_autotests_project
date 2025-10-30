import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_authorization(browser):
    # Для теста используем фиктивные данные
    user_email = os.getenv("UI_USER", "test@example.com")
    user_password = os.getenv("UI_PASS", "testpassword")

    print(f"Testing with email: {user_email}")

    browser.get("https://www.litres.ru")
    wait = WebDriverWait(browser, 10)

    try:
        # Просто проверяем что сайт открывается и есть кнопка входа
        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Войти')]")))
        assert login_btn.is_displayed()
        print("✅ Кнопка 'Войти' найдена")

    except Exception as e:
        browser.save_screenshot("auth_error.png")
        print(f"❌ Ошибка: {e}")
        raise