import time,info,db1,copy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
class dx():
    options = webdriver.ChromeOptions()
    # options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument('--headless')
    # options.add_argument('--disable-software-rasterizer')
    # options.set_preference("dom.webnotifications.serviceworker.enabled", False)
    # options.set_preference("dom.webnotifications.enabled", False)
    # options.add_argument('--headless')
    
def start():
    print('-----------------------------------------------------------------------')    
    start_time = time.time()
    db1.operators('createTenders')
    driver.get(info.website)    
    fulltime = round((time.time() - start_time),2)
def listAppender(webElement,list1):
    for i in webElement:
        list1.append(i.get_attribute('innerHTML'))
            
linksNotClean=[];links=[];sections=[];dates=[];times=[];counts=[];listOfAll = [];items = [];addresses=[]
def get_data():
    listOfAll.clear()
    linksNotClean.clear()
    links.clear()
    sections.clear()
    dates.clear()
    times.clear()
    counts.clear()
    items.clear()
    addresses.clear()    
    print('---Parsing...---') 
    webElements = driver.find_elements_by_xpath("//p/a[text()=' Информация о закупке ']")
    for i in webElements:
        linksNotClean.append(i.get_attribute('href'))
    print('ddddddddddddddd ')
    print(linksNotClean)    
    for i in linksNotClean:
        if "order-info" in i:
            if i not in links:
                links.append(i)
    getItems(links)

    print(links)
    #d.driver.switch_to_window(d.driver.window_handles[0])
    sectionEl = driver.find_elements_by_xpath("//div/p[@class='fs-12 grey-color fw-600']")
    dateToEndEl = driver.find_elements_by_xpath("//div/p[@class='fw-600 fs-12 m-0 grey-color']")
    #timeToEndEl = d.driver.find_elements_by_xpath("//div/p[@class='fs-12 m-0 grey-color fw-600 time_to_end']")
    countEl = driver.find_elements_by_xpath("//p[@class='fs-12 grey-color']/span[@class='fw-600 ws-nowrap']")
    listAppender(sectionEl,sections)
    listAppender(dateToEndEl,dates)
    listAppender(countEl,counts)
    listOfAll.append(links)
    listOfAll.append(sections)
    listOfAll.append(dates)
    listOfAll.append(times)
    listOfAll.append(counts)
    #listOfAll.append(datess)
    listOfAll.append(addresses)
    db1.operators('insert',listOfAll,items)
    print('%s items received from page' % '')
    print('--------------------')

def getItems(links):
    print('getItems def')
    inside = []
    for link in links:        
        #datess.append(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))        
        driver.execute_script("window.open('"+link + "', 'name')")
        driver.switch_to.window('name')        
        time.sleep(0.5)
        #timeEl = d.driver.find_elements_by_xpath("//div/div[@class='fs-14 grey-color col-md-9']")
        try:
            time.sleep(0.5)
            timeEl = driver.find_element_by_xpath("//div[contains(text(),' Дата и время окончания подачи ')]/following-sibling::div")
            times.append(timeEl.text)
        except(NoSuchElementException):
            times.append('Отсутствует')
        try:
            time.sleep(0.5)            
            addrEl = driver.find_element_by_xpath("//*[contains(text(),'или выполнение работ')]/following-sibling::div[@class='fs-14 grey-color col-md-9']/p")
            if(addrEl.get_attribute('address') != None):
                print(addrEl.get_attribute('address'))
                addresses.append(addrEl.get_attribute('address'))
            else:
                addrel = driver.find_element_by_xpath("//div[contains(text(),'адрес:')]/following-sibling::div")
                print('nonetry_адрес: ' + addrel.text)
                addresses.append(addrel.text)            
        except(NoSuchElementException):
            addrEl = driver.find_element_by_xpath("//*[contains(text(),'Адрес:')]/following-sibling::div")
            print('except_Адрес: ' + addrEl.text)
            addresses.append(addrEl.text)        
        itemEl = driver.find_elements_by_xpath("//tbody/tr")    
        for item in itemEl:
            s = item.get_attribute('name')
            inside.append(s)
        items.append(copy.deepcopy(inside))             
        #driver.switch_to_window(driverHandles)
        inside.clear()
# 

def parsing():
    for i in range(2,5,1):   
        get_data()
        print('Data received')
        time.sleep(1)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div/ul/li/button[@aria-label='Go to page " + str(i) + "']"))).click()
        time.sleep(1)
    get_data()

def runner():
    while True:
        db1.operators('drop tables')
        start()
        parsing()    
        #d.driver.close()
        
        time.sleep(420)
runner()

# now = datetime.datetime.now()
# today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
# today6pm = now.replace(hour=18, minute=0, second=0, microsecond=0)

# while True:
#     #if today8am < now < today6pm:
#     schedule.run_pending()
#     time.sleep(1)
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