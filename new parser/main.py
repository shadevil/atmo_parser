import time,info,db1,copy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get('https://zakaz.bashkortostan.ru/purchases/new')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# driver.maximize_window()
  
    
def listAppender(webElement,list1):
    for i in webElement:
        list1.append(i.get_attribute('innerHTML'))
        
class element:    
    def name(): return driver.find_element(By.XPATH,"//*[@id='__BVID__47']/div/p/a/text()")
    def inn(): return driver.find_element(By.XPATH,"//*[@id='text_row_49']")
    def kpp(): return driver.find_element(By.XPATH,"//*[@id='text_row_51']")
    def mailAddress(): return driver.find_element(By.XPATH,"//*[@id='text_row_53']")
    def category(): return driver.find_element(By.XPATH,"//*[@id='text_row_58']")
    def price(): return driver.find_element(By.XPATH,"//*[@id='text_row_price_66']")
    def deliveryAddress(): return driver.find_element(By.XPATH,"//*[@id='text_row_addresses_77']/li")
    
    
    def dateStart(): return driver.find_element(By.XPATH,"//*[@id='text_row_datetime_68']")
    def dateEnd(): return driver.find_element(By.XPATH,"//*[@id='text_row_datetime_70']")
    # def dateOfStart(dateStart):
        # return date(dateStart,"")
    # def dateOfEnd(dateEnd):
        # return date(dateEnd, "")   
    
    def fullList():
        return (name().get_attribute('innerHTML'), inn(), kpp(), mailAddress(), category(), price(), dateOfStart(dateStart), dateOfEnd(dateEnd), deliveryAddress())
    def fullListTest(self):
        return (self.__name()[0].get_attribute('innerHTML'), self.__inn()[0].get_attribute('innerHTML'), self.__kpp()[0].get_attribute('innerHTML'), self.__mailAddress()[0].get_attribute('innerHTML'), self.__category()[0].get_attribute('innerHTML'), self.__price()[0].get_attribute('innerHTML'), self.__dateStart()[0].get_attribute('innerHTML'), self.__dateEnd()[0].get_attribute('innerHTML'), self.__deliveryAddress()[0].get_attribute('innerHTML'))

        
def main():
    print('-----------------------------------------------------------------------')    
    start_time = time.time()
    db1.operators('createTenders')
      
    fulltime = round((time.time() - start_time),2)   
    print('---Parsing...---') 
    time.sleep(1)
    webElements = driver.find_elements(By.XPATH,"//p/a[text()=' Информация о закупке ']")
    items = []
    # for i in webElements:        
    driver.execute_script("window.open('" + webElements[0].get_attribute('href') + "', 'name')")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    itemsEl = driver.find_elements(By.XPATH,"//table/tbody/tr")
    time.sleep(1)
    for item in itemsEl:
            s = item.get_attribute('name')
            items.append(s)
    driver.switch_to.window(driver.window_handles[0])
    print(items)
if __name__ == "__main__":
    main()