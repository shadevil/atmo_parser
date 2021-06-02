import collections,multiprocessing,time,db
from selenium import webdriver
from itertools import product
from selenium.webdriver.common.keys import Keys
from pprint import pprint


listOfAll = []
start_time = time.time();
db.create_connection()

chromeOptions = webdriver.ChromeOptions() 
chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
chromeOptions.add_argument('--headless')
driver = webdriver.Chrome(options=chromeOptions, executable_path=r'C:\drivers\chromedriver.exe')
driver.get('https://zakaz.bashkortostan.ru/purchases/new')
fulltime = round((time.time() - start_time),2)
time.sleep(1)


def listAppender(search,list):
    place = []
    for i in search:
        list.append(i.get_attribute('innerHTML'))
            
linksNotClean=[];links=[];items=[];sections=[];dates=[];times=[];counts=[]
def get_data():    
    if links == []:
        print('---Lets parse---') 
    time.sleep(1)
    #webElements = driver.find_elements_by_partial_link_text('')
    webElements = driver.find_elements_by_xpath("//p/a[@class='system_link-style']")
    
    for i in webElements:
        linksNotClean.append(i.get_attribute('href'))
        
    for i in linksNotClean:
        if "order-info" in i:
            if i not in links:
                links.append(i)
                    
    sectionEl = driver.find_elements_by_xpath("//div/p[@class='fs-12 grey-color fw-600']")
    dateToEndEl = driver.find_elements_by_xpath("//div/p[@class='fw-600 fs-12 m-0 grey-color']")
    timeToEndEl = driver.find_elements_by_xpath("//div/p[@class='fs-12 m-0 grey-color fw-600 time_to_end']")
    countEl = driver.find_elements_by_xpath("//p[@class='fs-12 grey-color']/span[@class='fw-600 ws-nowrap']")
    #addressEl = driver.find_elements_by_xpath("//div[@class='my-2']/p[@class='fs-12 m-0 grey-color fw-600']")
    listAppender(sectionEl,sections)
    listAppender(dateToEndEl,dates)
    listAppender(timeToEndEl,times)
    listAppender(countEl,counts)
    
    count = len(links)
    print('%s items received' % count)
    print('--------------------')
    

def name():
    for link in links:
        driver.get(link)
        time.sleep(1)
        itemEl = driver.find_elements_by_xpath("//tbody/tr")    
        for item in itemEl:
            s = item.get_attribute('name')
            items.append(s)
    return items
         
def ccount(list):
    count = 0
    for item in list:
        count += len(item)
    return count

def main():    
    get_data()
    b2 = driver.find_element_by_xpath("(//button[@aria-label='Go to page 2'])[1]")
    b2.click()
    time.sleep(1)

    get_data()
    b3 = driver.find_element_by_xpath("(//button[@aria-label='Go to page 3'])[1]")
    b3.click()
    time.sleep(1)

    get_data()
    b4 = driver.find_element_by_xpath("(//button[@aria-label='Go to page 4'])[1]")
    b4.click()
    time.sleep(1)

    get_data()
    #print(len(links),len(dynamics),len(sections),len(dates),len(times),len(counts),len(addresses))
    

main()
listOfAll.append(links)
listOfAll.append(sections)
listOfAll.append(dates)
listOfAll.append(times)
listOfAll.append(counts)
db.insert('objects-base.db',listOfAll)
# for i in range(len(listOfAll)):
#     print(len(listOfAll[i]))
        

# print(ccount(listOfAll))
# for item in listOfAll:
#     print(listOfAll(item))
# print(ccount(times))
# print(ccount(counts))

driver.close()