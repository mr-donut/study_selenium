import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #ищем css переключатель
    first_integer = browser.find_element_by_css_selector('span#num1.nowrap').text
    second_integer = browser.find_element_by_css_selector('span#num2.nowrap').text
    x = str(int(first_integer)+int(second_integer))
    print(x)
    #раскрываем выпадающий список
    select = Select(browser.find_element_by_tag_name("select"))
    # ищем значение в списке
    select.select_by_visible_text(x)



    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()