"""
Web Scraping Project.

Purpose: Listing different SmartPhones along with their respective
characteristics and prices.

Source: Mercado Libre.
"""

from Driver import WebDriver
from DataFrameManager import DataFrameManager

driver = WebDriver('.\ChromeDriver\chromedriver')

driver.goTo('https://www.mercadolibre.com.ar/')
driver.search('CELULARES')
datos = driver.collect_data(60)

data_frame = DataFrameManager()
data_frame.append(datos)
data_frame.export()

driver.quit()
