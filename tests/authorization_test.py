import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.ui
def test_authorization(browser):
    base_url = os.getenv("BASE_URL", "https://www.litres.ru")
    user_email = os.getenv("UI_USER")
    user_password = os.getenv("UI_PASS")

    browser.get(base_url)
    wait = WebDriverWait(browser, 10)

    # Кнопка "Войти"
    enter_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.User-module__rQTUaW__wrapper'))
    )
    enter_button.click()

    # Ввод email
    login_input = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
    login_input.send_keys(user_email)

    # Кнопка "Далее"
    next_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.Button-module__cohrkq__buttonContent'))
    )
    next_button.click()

    # Ввод пароля
    password_input = wait.until(EC.presence_of_element_located((By.NAME, 'pwd')))
    password_input.send_keys(user_password)

    # Кнопка "Войти"
    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.Button-module__cohrkq__buttonContent'))
    )
    login_button.click()

    # Проверка успешного входа
    user_avatar = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.UserAvatar-module__avatar'))
    )
    assert user_avatar.is_displayed()
