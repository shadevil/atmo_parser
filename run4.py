import collections,multiprocessing,time
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

start_time = time.time();

chromeOptions = webdriver.ChromeOptions() 
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(options=chromeOptions, executable_path=r'C:\drivers\chromedriver.exe')
#action = ActionChains(driver)

driver.get('https://zakaz.bashkortostan.ru/purchases/new');

#time.sleep(3) # Let the user actually see something!

#element = driver.find_element_by_xpath("//div[@id='a']//a[@class='click']")
# timetoend = driver.find_elements_by_class_name('fs-18 m-0 grey-color fw-600 time_to_end') #Осталось до окончания приема предложений
# groups = driver.find_elements_by_class_name('fs-12 grey-color fw-600') #Группа закупки
# customers = driver.find_elements_by_xpath('p+a') #закупщик
# procurementLinks = driver.find_elements_by_xpath('a.system_link-style') # ссылка на закупку system_link-style
# #procurementLinks = driver.find_element_by_class_name('d-flex align-items-center green-color fs-12 fw-600 my-2') # ссылка на закупку system_link-style
# proposalLinks = driver.find_element_by_class_name('d-flex align-items-center green-color fs-12 fw-600 my-2') # ссылка на закупку system_link-style

fulltime = round((time.time() - start_time),2)
#element.get_attribute('innerHTML');
time.sleep(1)
asdasda = driver.find_elements_by_partial_link_text('')  #Информация о закупке 
print('---Lets parse---')
time.sleep(2)
for i in asdasda:
    print(i.get_attribute("href"))
print("--- %s seconds ---" % fulltime)

# window_before = driver.window_handles[0]


time.sleep(3) # Let the user actually see something!
driver.close()