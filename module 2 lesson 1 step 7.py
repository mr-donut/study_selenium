import math
from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)
    #ищем css переключатель
    x_element = browser.find_element_by_css_selector('img#treasure')
    #берем атрибут, ДЕЛАЕМ ИЗ СТРОКИ ЧИСЛО!
    x = int(x_element.get_attribute('valuex'))

    #вычисляем число
    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))

    x_element = browser.find_element_by_css_selector('#answer').send_keys(calc(x))

    option1 = browser.find_element_by_css_selector("#robotCheckbox").click()

    option2 = browser.find_element_by_css_selector("#robotsRule").click()

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()