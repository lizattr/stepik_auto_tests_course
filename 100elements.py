from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
    
    x = browser.find_element(By.ID, 'input_value').text
    result = calc(x)
    
    browser.find_element(By.ID, 'answer').send_keys(result)
    browser.find_element(By.ID, 'robotCheckbox').click()
    
    browser.execute_script("window.scrollBy(0, 100);")
    
    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.TAG_NAME, 'button').click()
    
finally:
    time.sleep(5)
    browser.quit()    