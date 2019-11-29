import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector('#input_value.nowrap')
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    x_element = browser.find_element_by_css_selector('#answer').send_keys(calc(x))

    option1 = browser.find_element_by_css_selector("#robotCheckbox").click()

    option2 = browser.find_element_by_css_selector("#robotsRule").click()

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    # browser.quit()