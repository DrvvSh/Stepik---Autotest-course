from selenium import webdriver
import os
import time

driver = webdriver.Chrome()

try:
    url = 'http://suninjuly.github.io/file_input.html'
    driver.get(url = url)
    
    firstName = driver.find_element_by_name("firstname").send_keys("Name")
    lastName = driver.find_element_by_name("lastname").send_keys("Nname")
    email = driver.find_element_by_name("email").send_keys("email@email.com")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    attach = driver.find_element_by_id("file").send_keys(file_path)
    time.sleep(1)
    
    submit = driver.find_element_by_css_selector(".btn").click()
finally:
    time.sleep(5)
    driver.quit()
    