import collections,multiprocessing,time,db
from selenium import webdriver
from itertools import product
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pprint import pprint

linksNotClean=[];links=[];sections=[];dates=[];times=[];counts=[];addresses=[];items=[]
listOfAll = []
start_time = time.time();
db.create_connection()

chromeOptions = webdriver.ChromeOptions() 
chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
#chromeOptions.add_argument('--headless')
driver = webdriver.Chrome(options=chromeOptions, executable_path=r'C:\drivers\chromedriver.exe')
#action = ActionChains(driver)
driver.get('https://zakaz.bashkortostan.ru/purchases/new')
fulltime = round((time.time() - start_time),2)
time.sleep(1)
def click_button(query):
    return driver.find_element_by_xpath(query)


def page_search(search,param):
    place = []
    if param == 'text':
        for i in search:
            place.append(i.get_attribute('innerHTML'))   
    
    return place    
def get_data():
    if links == []:
        print('---Lets parse---') 
    time.sleep(1)
    #webElements = driver.find_elements_by_partial_link_text('')
    webElements = driver.find_elements_by_xpath("//p/a[@class='system_link-style']")
    for i in webElements:    
        intermediate = i.get_attribute('href')
        linksNotClean.append(intermediate)
    for i in linksNotClean:
        if "order-info" in i:
            if i not in links:
                links.append(i)
                
    sectionEl = driver.find_elements_by_xpath("//div/p[@class='fs-12 grey-color fw-600']")
    dateToEndEl = driver.find_elements_by_xpath("//div/p[@class='fw-600 fs-12 m-0 grey-color']")
    timeToEndEl = driver.find_elements_by_xpath("//div/p[@class='fs-12 m-0 grey-color fw-600 time_to_end']")
    countEl = driver.find_elements_by_xpath("//p[@class='fs-12 grey-color']/span[@class='fw-600 ws-nowrap']")
    #addressEl = driver.find_elements_by_xpath("//div[@class='my-2']/p[@class='fs-12 m-0 grey-color fw-600']")
    listOfAll.append(page_search(sectionEl,'text'))
    listOfAll.append((page_search(dateToEndEl,'text')))
    listOfAll.append((page_search(timeToEndEl,'text')))
    listOfAll.append((page_search(countEl,'text')))
    
    count = len(links)
    print('%s items received' % count)
    print('--------------------')
    
def get_names():
    if links!=[]:
        for link in links:
            driver.get(link)
            time.sleep(1)
            itemEl = driver.find_elements_by_xpath("//tbody/tr")
            for item in itemEl:
                s = item.get_attribute('name')
                items.append(s)
                #print(s)
                
def ccount(list):
    count = 0
    for item in list:
        count += len(item)
    return count
def main():    
    get_data()
    click_button("(//button[@aria-label='Go to page 2'])[1]")
    time.sleep(1)

    get_data()
    click_button("(//button[@aria-label='Go to page 3'])[1]")
    time.sleep(1)

    get_data()
    click_button("(//button[@aria-label='Go to page 4'])[1]")
    time.sleep(1)

    get_data()
    click_button("(//button[@aria-label='Go to page 5'])[1]")
    
    get_data()
    #print(len(links),len(dynamics),len(sections),len(dates),len(times),len(counts),len(addresses))
    #db.insert('objects-base.db',links,dynamics,sections,dates,times,counts)

main()

for i in range(0, 19):
    for z in range(len(listOfAll)):
        print(listOfAll[z][i])
#print(items)
# print(ccount(listOfAll))
# for item in listOfAll:
#     print(listOfAll(item))
# print(ccount(times))
# print(ccount(counts))

driver.close()
   
#print('Worktime: %s seconds' % fulltime)

#element.get_attribute('innerHTML');

# window_before = driver.window_handles[0]

#element = driver.find_element_by_xpath("//div[@id='a']//a[@class='click']")
# timetoend = driver.find_elements_by_class_name('fs-18 m-0 grey-color fw-600 time_to_end') #Осталось до окончания приема предложений
# groups = driver.find_elements_by_class_name('fs-12 grey-color fw-600') #Группа закупки
# customers = driver.find_elements_by_xpath('p+a') #закупщик
# procurementLinks = driver.find_elements_by_xpath('a.system_link-style') # ссылка на закупку system_link-style
# #procurementLinks = driver.find_element_by_class_name('d-flex align-items-center green-color fs-12 fw-600 my-2') # ссылка на закупку system_link-style
# proposalLinks = driver.find_element_by_class_name('d-flex align-items-center green-color fs-12 fw-600 my-2') # ссылка на закупку system_link-style
