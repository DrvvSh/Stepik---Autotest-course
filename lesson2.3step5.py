from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    driver.get(link)
    button = driver.find_element_by_css_selector('.trollface').click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    x = driver.find_element_by_id('input_value').text
    y = calc(x)
    answer = driver.find_element_by_id('answer').send_keys(y)
    submit = driver.find_element_by_css_selector('.btn').click()

finally:
	time.sleep(5)
	driver.quit()