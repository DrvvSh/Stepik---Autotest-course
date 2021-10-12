from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
        
try: 
    link = "https://suninjuly.github.io/execute_script.html"
    driver = webdriver.Chrome()
    driver.get(link)
    
    x_element = driver.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    
    answer = driver.find_element_by_id('answer').send_keys(y)
    button = driver.find_element_by_tag_name("button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkBox = driver.find_element_by_id('robotCheckbox').click()
    radiobutton = driver.find_element_by_id('robotsRule').click()      
    button.click()    
    
    time.sleep(1)

finally:
    time.sleep(10)
    driver.quit()
    