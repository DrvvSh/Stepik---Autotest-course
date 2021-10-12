from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    driver.get(link)
    button = driver.find_element_by_css_selector('.btn').click()
    alert = driver.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    answer = driver.find_element_by_id('answer').send_keys(y)
    submit = driver.find_element_by_css_selector('.btn').click()

finally:
	time.sleep(5)
	driver.quit()