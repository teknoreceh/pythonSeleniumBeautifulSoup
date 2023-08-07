from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#fix autoclose error
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com")
driver.find_element(By.ID,'email').send_keys('Admin')
driver.find_element(By.ID, 'pass').send_keys('ryanramadhan')
driver.find_element(By.NAME,'login').click()