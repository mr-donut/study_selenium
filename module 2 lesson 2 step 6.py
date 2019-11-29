import math
from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #ищем css переключатель
    x = browser.find_element_by_css_selector('span#input_value.nowrap').text
    function_main = browser.find_element_by_css_selector('label span.nowrap').text
    function_main = (str(function_main).split(" ")[2]).replace(',', '').replace('ln', 'math.log').replace('sin', 'math.sin').replace('x', '')
    x = float(x)

    #вычисляем функцию
    def calc(x):
        return float(math.log(abs(12*math.sin(x))))
    #вставляем ответ
    x_element = browser.find_element_by_css_selector('#answer').send_keys(calc(x))

    # проматываем страничку вниз
    browser.execute_script("window.scrollBy(0, 100);")

    #отмечаем всякую хрень
    option1 = browser.find_element_by_css_selector("#robotCheckbox").click()
    option2 = browser.find_element_by_css_selector("#robotsRule").click()

    # нажимаем кнопку отправить
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()