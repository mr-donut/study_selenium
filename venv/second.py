# Поиск элементов с помощью Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
  # button = browser.find_element_by_id("submit_button")
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    browser.quit()