from selenium import webdriver
import time

try: 
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('.first_class input[required=""]')
    input1.send_keys('A')
    input2 = browser.find_element_by_css_selector('.second_class input[required=""]')
    input2.send_keys('B')
    input3 = browser.find_element_by_css_selector('.third_class input[required=""]')
    input3.send_keys('C')    

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
    