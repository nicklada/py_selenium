#!/usr/bin/env python3

# webdriver универсальный интерфейс, который позволяет манипулировать разными браузерами напрямую из кода
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    time.sleep(2)
finally:
    browser.quit()