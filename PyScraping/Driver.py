from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class WebDriver:
    def __init__(self, chromedriver):
        self.service = Service(chromedriver)
        self.options = Options()

        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')

        self.driver = webdriver.Chrome(service = self.service, options = self.options)
        self.wait = WebDriverWait(self.driver, 15)

    def goTo(self, webpage_link):
        try:
            self.driver.get(webpage_link)
            self.__waitFor('//body')
        except TimeoutError:
            print('Loading timed out. Process was cancelled.')
        
    def search(self, element):
        search_bar = self.__get_element('//input[@class="nav-search-input"]')

        search_bar.send_keys(element)
        search_bar.send_keys(Keys.RETURN)
    
    def collect_data(self, occurrs):
        element_link_xpath = '//ol/li//a[@class="ui-search-item__group__element shops__items-group-details ui-search-link"]'
        element_links = self.__get_elements(element_link_xpath)
        featured_elements = list()
        
        for element in element_links[:occurrs]:
            featured_elements.append(self.__get_features(element))
            element_links = self.__get_elements(element_link_xpath)
        
        return featured_elements
        
    def quit(self):
        self.driver.quit()
    
    def __moveTo(self, window):
        self.driver.switch_to.window(self.driver.window_handles[window])

    def __get_element(self, el_xpath):
        self.__waitFor(el_xpath)
        return self.driver.find_element(By.XPATH, el_xpath)
    
    def __get_elements(self, el_xpath):
        self.__waitFor(el_xpath)
        return self.driver.find_elements(By.XPATH, el_xpath)
    
    def __waitFor(self, el_xpath):
        self.wait.until(ec.presence_of_element_located((By.XPATH, el_xpath)))

    def __get_features(self, element):
        element.send_keys(Keys.CONTROL + Keys.RETURN)
        self.__moveTo(1)
        
        self.__get_element('//span[contains(@class,"ui-pdp-collapsable__action")]').send_keys(Keys.RETURN)

        data_tables = self.__get_elements('//table/tbody[@class="andes-table__body"]')

        data_dictionary = dict()

        for data_table in data_tables:
            data_rows = data_table.find_elements(By.XPATH, './/tr[contains(@class,"andes-table__row")]')

            for cells in data_rows:
                data_key = cells.find_element(By.XPATH, './/th[contains(@class, "andes-table__header")]').text
                data_value = cells.find_element(By.XPATH, './/td/span[contains(@class, "andes-table__column")]').text
                data_dictionary[data_key] = data_value

        self.driver.close()
        self.__moveTo(0)
        
        return data_dictionary
