import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YandexAuthTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.get("https://passport.yandex.ru/auth")
        self.assertIn("Авторизация", driver.title)

        # Введите ваш логин и пароль
        login_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "passp-field-login"))
        )
        login_field.send_keys("ya_login")
        login_field.send_keys(Keys.RETURN)

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "passp-field-passwd"))
        )
        password_field.send_keys("password")
        password_field.send_keys(Keys.RETURN)

        # Проверьте, что вы вошли в систему
        # Например, проверка наличия элемента, который доступен только после входа

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
