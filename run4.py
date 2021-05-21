import collections,multiprocessing,time
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pprint import pprint

linksNotClean = []
links = []
start_time = time.time();
chromeOptions = webdriver.ChromeOptions() 
chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
chromeOptions.add_argument('--headless')
driver = webdriver.Chrome(options=chromeOptions, executable_path=r'C:\drivers\chromedriver.exe')
#action = ActionChains(driver)
driver.get('https://zakaz.bashkortostan.ru/purchases/new')
fulltime = round((time.time() - start_time),2)
time.sleep(1)
butt2 = driver.find_element_by_xpath("(//button[@aria-label='Go to page 2'])[1]")
butt3 = driver.find_element_by_xpath("(//button[@aria-label='Go to page 3'])[1]")
butt4 = driver.find_element_by_xpath("(//button[@aria-label='Go to page 4'])[1]")

def get_links():
    if links == []:
        print('---Lets parse---')
    webElements = driver.find_elements_by_partial_link_text('')  #all links on page    
    time.sleep(1)
    
    for i in webElements:    
        intermediate = i.get_attribute('href')
        linksNotClean.append(intermediate)

    

    for i in linksNotClean:
        if "order-info" in i:
            if i not in links:
                links.append(i)

    count = len(links)
    print('%s links received' % count)
    print('--------------------')
get_links()

butt2.click()
time.sleep(2)

get_links()

butt3.click()
time.sleep(2)

get_links()

butt4.click()
time.sleep(2)

get_links()



#pprint(links)
print('Worktime: %s seconds' % fulltime)

driver.close()


#element.get_attribute('innerHTML');

# window_before = driver.window_handles[0]

#element = driver.find_element_by_xpath("//div[@id='a']//a[@class='click']")
# timetoend = driver.find_elements_by_class_name('fs-18 m-0 grey-color fw-600 time_to_end') #Осталось до окончания приема предложений
# groups = driver.find_elements_by_class_name('fs-12 grey-color fw-600') #Группа закупки
# customers = driver.find_elements_by_xpath('p+a') #закупщик
# procurementLinks = driver.find_elements_by_xpath('a.system_link-style') # ссылка на закупку system_link-style
# #procurementLinks = driver.find_element_by_class_name('d-flex align-items-center green-color fs-12 fw-600 my-2') # ссылка на закупку system_link-style
# proposalLinks = driver.find_element_by_class_name('d-flex align-items-center green-color fs-12 fw-600 my-2') # ссылка на закупку system_link-style
