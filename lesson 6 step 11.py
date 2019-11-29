from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = input(str())
    browser = webdriver.Chrome()
    browser.get(link)
    # список шаблонов обязательных полей с готовой выборкой
    xpath_list = ["// input[ @ placeholder = 'Input your first name']",
                  "// input[ @ placeholder = 'Input your last name']",
                  "// input[ @ placeholder = 'Input your email']"]
    for i in xpath_list:
        elements = browser.find_element(By.XPATH, i).send_keys("a_b_c_d_e_f_g")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)

    # закрываем браузер после всех манипуляций
    browser.quit()