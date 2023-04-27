"""
Web Scraping Project.

Purpose: Listing different SmartPhones along with their respective
characteristics and prices.

Source: Mercado Libre.
"""

from scrape_utils import Driver

driver = Driver()


driver.start('https://www.mercadolibre.com.ar/')


driver.quit()
