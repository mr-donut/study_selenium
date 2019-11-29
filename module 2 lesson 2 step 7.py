import os
from selenium import webdriver
import time

file = 'text.txt'
try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    #открываем файл на запись и сразу же закрываем
    with open(file, 'tw', encoding='utf-8') as f:
        pass
    f.close()
    #запоняем поля
    field_1 = browser.find_element_by_css_selector('input.form-control[name = firstname]').send_keys("1_2_3_4_5")

    field_2 = browser.find_element_by_css_selector("input.form-control[name = lastname]").send_keys("1_2_3_4_5")

    field_3 = browser.find_element_by_css_selector("input.form-control[name = email]").send_keys("1_2_3_4_5")

    upload_button = browser.find_element_by_css_selector("input#file")
    # разбираемся с абсолютным путем файла
    current_dir = os.path.abspath(os.path.dirname(file))
    #составляем путь файла из пути до него и самого имени файла
    file_path = os.path.join(current_dir, file)
    #нажимаем upload и вставляем туда полный путь
    upload_button.send_keys(file_path)

    # нажимаем кнопку отправить
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()