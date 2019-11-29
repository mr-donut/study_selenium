from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    elements = browser.find_elements_by_css_selector("input")
    for element in elements:

        # if "*" in element:
        element.send_keys("a_b_c_d_e_f_g")
        print(browser.find_elements_by_tag_name("label"))
        print(browser.find_elements_by_class_name("label"))
        print(browser.find_elements_by_partial_link_text("label"))
        # else:
        #     continue


    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
