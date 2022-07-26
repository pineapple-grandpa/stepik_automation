from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.ID, "input_value").text
answer = browser.find_element(By.ID, "answer")
answer.send_keys(calc(x))

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

radio = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit.click()

time.sleep(10)
browser.quit()
