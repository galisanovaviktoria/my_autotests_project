import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_authorization(browser):
    user_email = os.getenv("UI_USER")
    user_password = os.getenv("UI_PASS")

    browser.get("https://www.litres.ru")
    wait = WebDriverWait(browser, 15)

    try:
        # 1. Кликаем "Войти"
        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Войти']")))
        browser.execute_script("arguments[0].click();", login_btn)
        time.sleep(2)

        # 2. Вводим email
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_field.send_keys(user_email)

        # 3. Кликаем "Продолжить" через JavaScript
        continue_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Продолжить')]")))
        browser.execute_script("arguments[0].click();", continue_btn)
        time.sleep(2)

        # 4. Вводим пароль
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "pwd")))
        password_field.send_keys(user_password)

        # 5. Кликаем "Войти" через JavaScript
        submit_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Войти')]")))
        browser.execute_script("arguments[0].click();", submit_btn)
        time.sleep(3)

        # 6. Проверяем авторизацию
        profile_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Мой профиль') or contains(text(), 'Профиль')]"))
        )

        assert profile_element.is_displayed()

    except Exception as e:
        browser.save_screenshot("auth_error.png")
        raise