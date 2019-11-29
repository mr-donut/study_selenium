from selenium import webdriver
import time
import math

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    #нажать на кнопку посреди страницы
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()
    time.sleep(1)
    #нажать на подтверждение во всплывающем окне
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    # ищем css переключатель
    x = browser.find_element_by_css_selector('span#input_value.nowrap').text
    x = float(x)
    # вычисляем функцию
    def calc(x):
        return float(math.log(abs(12 * math.sin(x))))
    print(calc(x))
    # вставляем ответ captcha
    x_element = browser.find_element_by_css_selector('#answer').send_keys(calc(x))

    # нажимаем кнопку отправить
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()