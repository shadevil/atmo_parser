import collections,multiprocessing,time,info,datetime,schedule,db1
from selenium import webdriver
from itertools import product
from selenium.webdriver.common.keys import Keys
from pprint import pprint

class d():
    chromeOptions = webdriver.ChromeOptions() 
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    chromeOptions.add_argument('--headless')
    driver = webdriver.Chrome(options=chromeOptions, executable_path=r'chromedriver.exe')  
def start():
    print('-----------------------------------------------------------------------')    
    start_time = time.time();
    
    db1.operators('createTenders')
    db1.operators('createItems')
    d.driver.get(info.website)
    fulltime = round((time.time() - start_time),2)
    time.sleep(0.5)
def listAppender(webElement,list1):
    for i in webElement:
        list1.append(i.get_attribute('innerHTML'))
            
linksNotClean=[];links=[];items=[];sections=[];dates=[];times=[];counts=[];inside=[];listOfAll = []
def get_data():
    listOfAll.clear()
    linksNotClean.clear()
    links.clear()
    items.clear();
    sections.clear()
    dates.clear()
    times.clear()
    counts.clear()
    inside.clear()
    
    print('---Parsing...---') 
    time.sleep(0.5)
    webElements = d.driver.find_elements_by_xpath("//p/a[@class='system_link-style']")
    
    for i in webElements:
        linksNotClean.append(i.get_attribute('href'))
        
    for i in linksNotClean:
        if "order-info" in i:
            if i not in links:                
                links.append(i)
                name(i)
               
    sectionEl = d.driver.find_elements_by_xpath("//div/p[@class='fs-12 grey-color fw-600']")
    dateToEndEl = d.driver.find_elements_by_xpath("//div/p[@class='fw-600 fs-12 m-0 grey-color']")
    timeToEndEl = d.driver.find_elements_by_xpath("//div/p[@class='fs-12 m-0 grey-color fw-600 time_to_end']")
    countEl = d.driver.find_elements_by_xpath("//p[@class='fs-12 grey-color']/span[@class='fw-600 ws-nowrap']")
    #addressEl = driver.find_elements_by_xpath("//div[@class='my-2']/p[@class='fs-12 m-0 grey-color fw-600']")
    listAppender(sectionEl,sections)
    listAppender(dateToEndEl,dates)
    listAppender(timeToEndEl,times)
    listAppender(countEl,counts)
    listOfAll.append(links)
    listOfAll.append(sections)
    listOfAll.append(dates)
    listOfAll.append(times)
    listOfAll.append(counts)
    #pprint(listOfAll)
    #pprint(items)
    
    db1.operators('insert',listOfAll,items)
    print('%s items received from page' % '')
    print('--------------------')

def name(link):
    
    d.driver.execute_script("window.open('"+link + "', 'name')")
    d.driver.switch_to.window('name')
    time.sleep(0.5)
    itemEl = d.driver.find_elements_by_xpath("//tbody/tr")    
    for item in itemEl:
        s = item.get_attribute('name')
        inside.append(s)
    items.append(inside)
    d.driver.close()
    #driver.switch_to_window(driverHandles)
    d.driver.switch_to_window(d.driver.window_handles[0])
    
# 

def parsing():
    for i in range(2,5,1):
    #i = 2     
        get_data()    
        b2 = d.driver.find_element_by_xpath("(//button[@aria-label='Go to page " + str(i) + "'])[1]")
        b2.click()
        time.sleep(0.5)
    get_data()
    d.driver.close()

def runner():
    start()
    parsing()

def dropTables():
    db1.operators('drop tables')
#main()
schedule.every(5).minutes.do(runner)
schedule.every(2).days.do(dropTables)
# now = datetime.datetime.now()
# today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
# today6pm = now.replace(hour=18, minute=0, second=0, microsecond=0)

while True:
    #if today8am < now < today6pm:
    schedule.run_pending()
    time.sleep(1)
# today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
# today6pm = now.replace(hour=18, minute=0, second=0, microsecond=0)
# schedule.every(10).minutes.do(do())
# schedule.every(2).days.do(db1.operators('drop tables'))

# lasttime = now
# while True:
#     if now > today8am and now < today6pm:        
# #schedule.run_pending()
#         time.sleep(0.5)
#         print('time from 8 to 18')
#     if now == today6pm:
#         db1.operators('drop tables')
#         print('drop tables')

# for i in range(len(listOfAll)):
#     print(len(listOfAll[i]))
        

# print(ccount(listOfAll))
# for item in listOfAll:
#     print(listOfAll(item))
# print(ccount(times))
# print(ccount(counts))


#def ccount(list1):
    #     count = 0
#     for item in list1:
#         count += len(item)
#     return count
# lasttime=datetime.datetime.now()

# while (lasttime + timedelta(minutes=10)) < datetime.datetime.now():
#     lasttime = datetime.datetime.now()
#     start()
#     parsing()