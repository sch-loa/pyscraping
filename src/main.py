"""
The WebDriver class from the Driver module provides all the methods required to collect data from the website,
while the DataFrameManager class from the DataFrameManager module is in charge of exporting data as a .xlsx file.
"""

from Driver import WebDriver
from DataFrameManager import DataFrameManager

product_name = input("Name of the product: ")
occurrs = int(input("Maximum number of occurrences: "))

# Specifies route to the ChromeDriver file, if you wanna use another version you should be able to
# by replacing the existing file for the new one and changing the name of the file if necessary.
driver = WebDriver('.\ChromeDriver\chromedriver')
data_frame = DataFrameManager()

# Navigates to the website and collects the data result of the given search parameter.
driver.goTo('https://www.mercadolibre.com.ar/')
driver.search(product_name)
datos = driver.collect_data(occurrs)

# Exports data returned from the WebDriver.
data_frame.append(datos)
data_frame.export(product_name)

driver.quit()
