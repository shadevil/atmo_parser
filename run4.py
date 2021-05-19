import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:\drivers\chromedriver.exe')

driver.get('https://zakaz.bashkortostan.ru/purchases/new');

#time.sleep(3) # Let the user actually see something!

elements = driver.find_elements_by_class_name("""purchase_part""")
print(len(elements))

#time.sleep(3) # Let the user actually see something!

driver.close()