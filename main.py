from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#fix autoclose error
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver.get('https://www.google.com')
driver.maximize_window()
# Identifikasi elemen kolom pencarian dengan cara mengidentifikasi 
# elemen input dengan atribut 'name' atau 'id' yang sesuai
search_box = driver.find_element("name", "q")
# Ketikkan "berita politik hari ini" ke dalam kolom pencarian
search_box.send_keys("berita politik hari ini")

# Submit pencarian (opsional, tergantung pada situs target)
search_box.submit()

# Tunggu beberapa saat untuk melihat hasil pencarian
driver.implicitly_wait(5)
