from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    driver = webdriver.Chrome()
    driver.get(link)    
     
    valueX = driver.find_element_by_id('treasure').get_attribute('valuex')
        
    answer = driver.find_element_by_id('answer').send_keys(calc(valueX))
    checkBox = driver.find_element_by_id('robotCheckbox').click()
    radiobutton = driver.find_element_by_id('robotsRule').click()
    
    button = driver.find_element_by_css_selector(".btn.btn-default").click()
    
    time.sleep(1)

finally:
    time.sleep(10)
    driver.quit()
    