import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_authorization(browser):
    user_email = os.getenv("UI_USER")
    user_password = os.getenv("UI_PASS")

    # Проверяем что переменные установлены
    if not user_email or not user_password:
        raise ValueError("Не установлены переменные окружения UI_USER или UI_PASS")

    browser.get("https://www.litres.ru")
    wait = WebDriverWait(browser, 15)

    try:
        # Кликаем "Войти"
        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Войти']")))
        browser.execute_script("arguments[0].click();", login_btn)
        time.sleep(2)

        # Вводим email
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_field.send_keys(user_email)

        # Кликаем "Продолжить"
        continue_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Продолжить')]")))
        browser.execute_script("arguments[0].click();", continue_btn)
        time.sleep(2)

        # Вводим пароль
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "pwd")))
        password_field.send_keys(user_password)

        # Кликаем "Войти"
        submit_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Войти')]")))
        browser.execute_script("arguments[0].click();", submit_btn)
        time.sleep(3)

        # Проверяем авторизацию
        profile_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Мой профиль') or contains(text(), 'Профиль')]"))
        )

        assert profile_element.is_displayed()

    except Exception as e:
        browser.save_screenshot("auth_error.png")
        raise