from selenium import webdriver
import time
import math

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # нажимаем кнопку
    button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
    button.click()

    # запомнить имя текущей вкладки
    first_window = browser.window_handles[0]

    # выбираем вторую вкладку
    new_window = browser.window_handles[1]

    # Для переключения на новую вкладку надо явно указать, на какую
    browser.switch_to.window(new_window)

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