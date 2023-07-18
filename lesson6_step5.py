#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://www.degreesymbol.net/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #мы хотим найти ссылку с текстом "Degree symbol in Math" и перейти по ней
    link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
    link.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
