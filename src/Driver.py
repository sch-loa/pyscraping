from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#Generic Web Management
class WebDriverEssentials:
    # Initializes the Chrome WebDriver with the required parameters.
    def __init__(self, chromedriver):
        self.service = Service(chromedriver)
        self.options = Options()

        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')

        self.driver = webdriver.Chrome(service = self.service, options = self.options)
        self.wait = WebDriverWait(self.driver, 15)

    # Navigates to the given webpage link.
    def goTo(self, webpage_link):
        self.driver.get(webpage_link)
        self._waitFor('//body')

    # Closes WebDriver
    def quit(self):
        self.driver.quit()
    
    # Moves to another tab
    def _moveTo(self, window):
        self.driver.switch_to.window(self.driver.window_handles[window])

    # Returns a single element that satisfies a given XPATH
    def _get_element(self, el_xpath):
        self._waitFor(el_xpath)
        return self.driver.find_element(By.XPATH, el_xpath)
    
    # Returns a list of elements that satisfy a given XPATH
    def _get_elements(self, el_xpath):
        self._waitFor(el_xpath)
        return self.driver.find_elements(By.XPATH, el_xpath)
    
    # Waits for a given element to load in the webpage.
    # If it doesn't load within the specified 15 seconds, it raises an exception.
    def _waitFor(self, el_xpath):
        try:
            self.wait.until(ec.presence_of_element_located((By.XPATH, el_xpath)))
        except TimeoutException:
            raise Exception('Loading timed out. Process was cancelled.')

class WebDriver(WebDriverEssentials):
    # Looks for specific products using the search bar.
    def search(self, element):
        search_bar = self._get_element('//input[@class="nav-search-input"]')

        search_bar.send_keys(element)
        search_bar.send_keys(Keys.RETURN)
    

    # Gets the links for every product in the current webpage and, one by one, navigates
    # to them in another tab in order to collect the technical features and prices of every single one. If necessary,
    # it repeats the same process in next page. It returns a list of dictionaries that contain the data.
    def collect_data(self, occurrs):
        element_link_xpath = '//ol/li//a[@class="ui-search-item__group__element shops__items-group-details ui-search-link"]'
        next_page_bttn_xpath = '//ul/li[contains(@class, "andes-pagination__button--next")]//a[contains(@class, "andes-pagination__link")]'
        featured_elements = list()

        while(occurrs > 0):
            element_links = self._get_elements(element_link_xpath)

            for element in element_links:
                featured_elements.append(self._get_features(element))
                element_links = self._get_elements(element_link_xpath)

                occurrs -= 1
                
                if(occurrs == 0):
                    break

            try:
                next_page_bttn = self._get_element(next_page_bttn_xpath)
                next_page_bttn.send_keys(Keys.RETURN)
            except:
                break

        return featured_elements
    
    # Navigates to the specific product's webpage and collects the necessary information about it.
    # It returns a dictionary that contains the data.
    def _get_features(self, element):
        element.send_keys(Keys.CONTROL + Keys.RETURN)
        self._moveTo(1)
        
        try:
            self._get_elements('//span[contains(@class,"ui-pdp-collapsable__action")]')[0].send_keys(Keys.RETURN)
        except:
            pass

        data_tables = self._get_elements('//div//table[@class="andes-table"]/tbody[@class="andes-table__body"]')

        data_dictionary = dict()

        for data_table in data_tables:
            data_rows = data_table.find_elements(By.XPATH, './/tr[contains(@class,"andes-table__row")]')

            for cells in data_rows:
                data_key = cells.find_element(By.XPATH, './/th[contains(@class, "andes-table__header")]').text
                data_value = cells.find_element(By.XPATH, './/td/span[contains(@class, "andes-table__column")]').text
                data_dictionary[data_key] = data_value

                price = self._get_element('//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]')
                data_dictionary["Precio"] = price.text

        self.driver.close()
        self._moveTo(0)
        
        return data_dictionary
