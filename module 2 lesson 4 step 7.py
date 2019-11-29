from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 11 секунд, пока появится определенный текст
    condition = WebDriverWait(browser, 11).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    # жмем button
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

    # перематываем окно
    browser.execute_script("window.scrollBy(0, 50);")
    x = browser.find_element_by_css_selector('span#input_value.nowrap').text
    x = float(x)

    # вычисляем функцию
    def calc(x):
        return float(math.log(abs(12 * math.sin(x))))
    print(calc(x))

    # вставляем ответ captcha
    x_element = browser.find_element_by_css_selector('#answer').send_keys(calc(x))

    # нажимаем кнопку отправить
    button = browser.find_element_by_css_selector("#solve.btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать ответ с всплывающего окна
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()