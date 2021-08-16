from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


def findPriceInformation():
    # path to selenium chrome driver
    path = ('./chromedriver_win32/chromedriver.exe')
    driver = webdriver.Chrome(path)
    
    # then open a website using selenium driver
    driver.get('https://www.nseindia.com/')
    # delete all cookies
    driver.delete_all_cookies()
    # find the search box using id attribute
    search_box_id="header-search-input"
    search = driver.find_element_by_id(search_box_id)
    # write text inside box
    search.send_keys("ADITYA BIRLA CAPITAL LIMITED")
    time.sleep(4)
    # select desired dropdown using down arrow key
    search.send_keys(Keys.DOWN)
    # press enter
    search.send_keys(Keys.RETURN)
    time.sleep(4)
    # find id attribute of price span tag
    price_id = "quoteLtp"
    search_price = driver.find_element_by_id(price_id)
    # print text of span tag(price)
    print("price: ", search_price.text)
    
    driver.close()
    driver.quit()
    
    
if __name__ == "__main__":
    findPriceInformation()

    