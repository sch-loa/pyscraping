"""
Web Scraping Project.

Purpose: Listing different SmartPhones along with their respective
characteristics and prices.

Source: Mercado Libre.
"""

from Driver import WebDriver

driver = WebDriver('.\ChromeDriver\chromedriver')

driver.goTo('https://www.mercadolibre.com.ar/')
driver.search('CELULARES')

datos = driver.collect_data()

print(datos)
driver.quit()
