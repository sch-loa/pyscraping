"""
Web Scraping Project.

Purpose: Listing different SmartPhones along with their respective
characteristics and prices.

Source: Mercado Libre.
"""

from scrape_utils import Driver

driver = Driver('.\ChromeDriver\chromedriver')

driver.start('https://www.mercadolibre.com.ar/')
driver.search('CELULARES')

driver.quit()
