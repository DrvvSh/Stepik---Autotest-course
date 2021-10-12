from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

driver = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
driver.find_element_by_id('book').click()

x = driver.find_element_by_id('input_value').text
y = calc(x)
answer = driver.find_element_by_id('answer').send_keys(y)
submit = driver.find_element_by_id('solve').click()

time.sleep(5)
driver.quit()