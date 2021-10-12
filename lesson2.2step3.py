from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

#def calc(x, y):
    #return str(x + y)
try: 
    link = "http://suninjuly.github.io/selects1.html"
    driver = webdriver.Chrome()
    driver.get(link)    
     
    x = driver.find_element_by_id('num1').text
    y = driver.find_element_by_id('num2').text
    sum = str(int(x) + int(y))   
    
    select = Select(driver.find_element_by_tag_name("select"))
    select.select_by_value(sum)
    button = driver.find_element_by_css_selector(".btn.btn-default").click()
    
    time.sleep(1)

finally:
    time.sleep(10)
    driver.quit()
    
