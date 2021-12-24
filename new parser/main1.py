from os import link
import time,copy,db1
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException as NSE
from selenium.common.exceptions import TimeoutException as TE

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get('https://zakaz.bashkortostan.ru/purchases/new')
options = webdriver.ChromeOptions()
# driver.maximize_window()

def getLinks():
    links = []
    # aria-checked="true"
    # firstBtn = driver.find_element(By.XPATH("//*[@id='content-block']/div[1]/div/ul/li[1]/button"))
    # previousBtn = driver.find_element(By.XPATH("//*[@id='content-block']/div[1]/div/ul/li[2]/button"))
    wait = WebDriverWait(driver,5)
    lastBtn = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='content-block']/div[1]/div/ul/li[9]/button")))
    lastBtn.click()
    endNum = driver.find_element(By.XPATH,"//*[@id='content-block']/div[1]/div/ul/li[7]/button").get_attribute('aria-posinset')
    firstBtn = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='content-block']/div[1]/div/ul/li[1]/button")))
    firstBtn.click()
    print(endNum)
    i=1
    try:
        while True:
            time.sleep(1)
            setarr = set(links)
            if len(links) == len(setarr):
                print("Loading page " + str(i) + "...")
                linkElements = wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//p/a[text()=' Информация о закупке ']")))
                for link in linkElements:
                    links.append(link.get_attribute('href'))
                    print(link.get_attribute('href'))
                print("Page " + str(i) + " loaded")
                nextBtnLink = "//*[@id='content-block']/div[1]/div/ul/li[8]/button"
                if(i < int(endNum)):
                    time.sleep(1)
                    driver.find_element(By.XPATH,nextBtnLink).click()
                else:
                    break
                i+=1
                
        if (len(links)>0):
            x = len(links)
            print("Ссылок получено: " + str(x))
            return links
    except(NSE):
        print('Веб-элемент не найден.')
    except(TE):
        print('Истекло время ожидания веб-элемента')
        
class Tender:
    def __init__(self,link):
        self.name = driver.find_element(By.XPATH,"//*[@id='__BVID__47']/div/p/a").text
        self.kpp = driver.find_element(By.XPATH,"//*[@id='text_row_51']").get_attribute('innerHTML')
        self.mailAddress = driver.find_element(By.XPATH,"//*[@id='text_row_53']").get_attribute('innerHTML')
        self.category = driver.find_element(By.XPATH,"//*[@id='text_row_58']").get_attribute('innerHTML')
        self.price = driver.find_element(By.XPATH,"//*[@id='text_row_price_66']").get_attribute('innerHTML')
        self.deliveryAddress = driver.find_element(By.XPATH,"//*[@id='text_row_addresses_77']/li").get_attribute('innerHTML')
        self.itemsEl = driver.find_elements(By.XPATH,"//table/tbody/tr")
        self.dynamics = "0"    
        self.dateStart = driver.find_element(By.XPATH,"//*[@id='text_row_datetime_68']").get_attribute('innerHTML')
        self.dateEnd = driver.find_element(By.XPATH,"//*[@id='text_row_datetime_70']").get_attribute('innerHTML')
        self.link = link
        self.items = self.getItems()
    # def dateOfStart(dateStart):
        # return date(dateStart,"")
    # def dateOfEnd(dateEnd):
        # return date(dateEnd, "")   
    
    # def fullListTest():
    #     return [name.get_attribute('innerHTML'), inn, kpp, mailAddress, category, price, dateOfStart(dateStart), dateOfEnd(dateEnd), deliveryAddress]
    def getItems(self):        
        inside = ""
        for item in self.itemsEl:
            s = item.get_attribute('name')
            inside = inside + "//" + s
        # fullList = [self.name, self.inn.get_attribute('innerHTML'), self.kpp.get_attribute('innerHTML'), self.mailAddress.get_attribute('innerHTML'), self.category.get_attribute('innerHTML'), self.price.get_attribute('innerHTML'), self.deliveryAddress.get_attribute('innerHTML'), self.link, self.dateStart.get_attribute('innerHTML'), self.dateEnd.get_attribute('innerHTML'),inside]
        return inside
        
        

        
        
def main():
    print('-----------------------------------------------------------------------')    
    db1.operators('createTenders') 
    print('---Load links...---') 
    time.sleep(1)
    links = getLinks()
    # print('---Load tenders...---')
    # for link in links:
    #     driver.execute_script("window.open('" + link + "', 'name')")
    #     driver.switch_to.window(driver.window_handles[1])
    #     time.sleep(2)
    #     db1.operators('insert',Tender(link))
    #     driver.switch_to.window(driver.window_handles[0])
    
if __name__ == "__main__":
    main()