import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestReg(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first[required]")
        first_name.send_keys("name")

        last_name = browser.find_element(By.CSS_SELECTOR, ".second[required]")
        last_name.send_keys("last name")

        email = browser.find_element(By.CSS_SELECTOR, ".third[required]")
        email.send_keys("email")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            welcome_text,
            "Conlations! You gratuhave successfully registered!",
            f"expected Congratulations! You have successfully registered!, got {welcome_text}",
        )

        time.sleep(10)
        browser.quit()

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first[required]")
        first_name.send_keys("name")

        last_name = browser.find_element(By.CSS_SELECTOR, ".second[required]")
        last_name.send_keys("last name")

        email = browser.find_element(By.CSS_SELECTOR, ".third[required]")
        email.send_keys("email")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!",
            f"expected Congratulations! You have successfully registered!, got {welcome_text}",
        )

        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
