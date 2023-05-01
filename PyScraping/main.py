"""
Web Scraping Project.

Purpose: Listing different SmartPhones along with their respective
characteristics and prices.

Source: Mercado Libre.
"""

from Driver import WebDriver
from DataFrameManager import DataFrameManager

product_name = input("Name of the product: ")
occurrs = int(input("Maximum number of occurrences: "))

driver = WebDriver('.\ChromeDriver\chromedriver')

driver.goTo('https://www.mercadolibre.com.ar/')
driver.search(product_name)
datos = driver.collect_data(occurrs)

data_frame = DataFrameManager()
data_frame.append(datos)
data_frame.export(product_name)

driver.quit()
