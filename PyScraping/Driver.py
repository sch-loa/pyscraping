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
        self.wait = WebDriverWait(self.driver, 10)

    def goTo(self, webpage_link):
        self.driver.get(webpage_link)
        self.__waitFor('//body')

    def __get_search_bar(self, el_path):
        return self.driver.find_element(By.XPATH, el_path)

    def search(self, element):
        search_bar = self.__get_search_bar('//input[@class="nav-search-input"]')

        search_bar.send_keys(element)
        search_bar.send_keys(Keys.RETURN)
    
    def __get_elements(self, el_xpath):
        return self.driver.find_elements(By.XPATH, el_xpath)
    
    def __waitFor(self, el_xpath):
        self.wait.until(ec.presence_of_element_located((By.XPATH, el_xpath)))

    def __get_feat_bttn(self, el_xpath):
        return self.driver.find_element(By.XPATH, el_xpath)

    def __check_features(self, element):
        feat_bttn_xpath = '//a[@class="ui-pdp-media__action ui-vpp-highlighted-specs__features-action"]'
        
        element.send_keys(Keys.RETURN)
        self.__waitFor(feat_bttn_xpath)

        self.__get_feat_bttn(feat_bttn_xpath).send_keys(Keys.RETURN)

        
        """
        brand = element.send_keys(Keys.)
        line =
        model =
        ram =
        storage = 
        price =

        template = {'brand': brand,
                    'line': line,
                    'model': model,
                    'ram': ram,
                    'storage': storage,
                    'price': price}

        return template
        """

    def collect_data(self):
        elements = self.__get_elements('//ol/li//a[@class="ui-search-link"]')
        featured_elements = list()
        self.__check_features(elements[0])
        #for i in elements:
        #featured_elements.append(self.__check_features(elements[0]))

        return featured_elements
        

    def quit(self):
        self.driver.quit()