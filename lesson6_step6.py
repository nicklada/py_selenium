#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("hi")
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла
