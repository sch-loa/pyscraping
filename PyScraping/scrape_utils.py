from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Driver():
    def __init__(self, chromedriver):
        self.service = Service(chromedriver)
        self.options = Options()

        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')

        self.driver = webdriver.Chrome(service = self.service, options = self.options)
        self.wait = WebDriverWait(self.driver, 10)

    def start(self, webpage_link):
        self.driver.get(webpage_link)
        
        self.wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))

    def __get_search_bar(self):
        return self.driver.find_element(By.ID, 'cb1-edit')

    def search(self, element):
        search_bar = self.__get_search_bar()

        search_bar.send_keys(element)
        search_bar.send_keys(Keys.RETURN)
        

    def quit(self):
        self.driver.quit()