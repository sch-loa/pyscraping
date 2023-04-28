from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class WebDriver():
    def __init__(self, chromedriver):
        self.service = Service(chromedriver)
        self.options = Options()

        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')

        self.driver = webdriver.Chrome(service = self.service, options = self.options)
        self.wait = WebDriverWait(self.driver, 15)

    def goTo(self, webpage_link):
        self.driver.get(webpage_link)
        self.__waitFor('//body')
        
    def search(self, element):
        search_bar = self.__get_element('//input[@class="nav-search-input"]')

        search_bar.send_keys(element)
        search_bar.send_keys(Keys.RETURN)
    
    def collect_data(self):
        element_link_xpath = '//ol/li//a[@class="ui-search-item__group__element shops__items-group-details ui-search-link"]'
        element_links = self.__get_elements(element_link_xpath)
        featured_elements = list()
        
        for element in element_links[:3]:
            featured_elements.append(self.__get_features(element))
            element_links = self.__get_elements(element_link_xpath)
        
        return featured_elements
        
    def quit(self):
        self.driver.quit()

    def __get_element(self, el_xpath):
        return self.driver.find_element(By.XPATH, el_xpath)
    
    def __get_elements(self, el_xpath):
        return self.driver.find_elements(By.XPATH, el_xpath)
    
    def __waitFor(self, el_xpath):
        self.wait.until(ec.presence_of_element_located((By.XPATH, el_xpath)))

    def __get_features(self, element):
        feat_bttn_xpath = '//a[contains(@class,"ui-pdp-media__action")]'
        data_tables_xpath = '//table/tbody[@class="andes-table__body"]'

        element.send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.switch_to.window(self.driver.window_handles[1])
        
        self.__waitFor(feat_bttn_xpath)
        self.__get_element(feat_bttn_xpath).send_keys(Keys.RETURN)

        self.__waitFor(data_tables_xpath)
        data_tables = self.__get_elements(data_tables_xpath)

        data_dictionary = dict()
        for data_table in data_tables:
            data_rows = data_table.find_elements(By.XPATH, './/tr[contains(@class,"andes-table__row")]')

            for cells in data_rows:
                data_key = cells.find_element(By.XPATH, './/th[contains(@class, "andes-table__header")]').text
                data_value = cells.find_element(By.XPATH, './/td/span[contains(@class, "andes-table__column")]').text
                data_dictionary[data_key] = data_value
        
        print(data_dictionary)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        return data_dictionary
