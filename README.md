# PyScraping
Web Scraping using Python and Selenium WebDriver.

The purpose of this project is to list different products from **Mercado Libre** based on a specific search in order to store them in a data base (which would be a .xlsx file, in this scenario). Given the generic way the elements are located on the website it should be able to work regardless of what you're searching for.

The program needs two input values: a search parameter and a maximum number of occurrences of the product (if the amount of occurrences in the website were lower than that value, it would then list the total amount).

It works by going through every product located on the website (in order, result of the specific search parameter) one by one and collecting all the data related to its technical features, plus its price. Then going back to do the same with the next one. The data of every product is stored in a dictionary, and every dictionary is placed inside a list. Once the specified amount of products has been listed, the data is converted to a DataFrame, and it is finally exported as a .xlsx file and saved inside the DataBases directory. Each file gets named with the search parameter and the date and time it was created at.

You may notice that there are already two files inside of the DataBases folder. Those are the result of running the program for two different searchs: "CELULARES" for 100 occurrences, and "COMPUTADORAS DE ESCRITORIO" for 50 occurrences, respectively.

# Versions
- **Python 3.11.1**
  - selenium 4.7.2
  - pandas 2.0.0
  - datetime 5.1
- **ChromeDriver 112.0.5615.49**
