import time
from selenium import webdriver
driver = webdriver.Chrome('C:/Drivers/chrome/chromedriver.exe')
driver.get('http://google.com');
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('Searchhhh')
search_box.submit()
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
time.sleep(10)
driver.quit()