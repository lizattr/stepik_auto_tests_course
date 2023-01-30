from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://kz.stage-alpha.dogovor24.dev/login")
    
    browser.find_element(By.ID, 'login-input__email_phone_input').send_keys('k.elizaveta+123@dogovor24.kz')
    browser.find_element(By.ID, 'login-input__submit_button').click()
    time.sleep(5)
    browser.find_element(By.ID, 'pass-input__password_input').send_keys('nB4mHyMhjb')
    browser.find_element(By.ID, 'pass-input__submit_button').click()
    print('login ok')
        
finally:
    time.sleep(5)
    browser.quit()    