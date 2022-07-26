from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("somebody")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("someone")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@test.com")

    filepicker = browser.find_element(By.NAME, "file")
    filepicker.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    time.sleep(8)
    browser.quit()
