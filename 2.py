from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
options.page_load_strategy = 'none'
driver.get("http://www.google.com")
# driver.quit()