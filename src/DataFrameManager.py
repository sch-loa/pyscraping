import pandas as pd
import os
from datetime import datetime

class DataFrameManager:
    # Creates an empty DataFrame
    def __init__(self):
        self.dataframe = pd.DataFrame()

    # Adds a list of dictionaries to the DataFrame
    def append(self, data_dicts):
        for data_dict in data_dicts:
            data_dict = pd.DataFrame(data_dict, index = range(1))
            if(self.dataframe.empty):
                self.dataframe = data_dict
            else:
                self.dataframe = pd.concat([self.dataframe, data_dict], axis = 0, ignore_index = True)
    
    # Exports DataFrame as a .xlsx file through an specific route that, if it didn't exist it'd created.
    def export(self, product_name):
        dirr = './DataBases/'

        product_name = product_name.strip()
        product_name = product_name.replace(" ", "_")

        if(not os.path.exists(dirr)):
            os.makedirs(dirr)
        date_and_hour = datetime.now().strftime('(%Y-%m-%d_%Hhs%Mmins)')
        self.dataframe.to_excel(f'{dirr}{product_name}_{date_and_hour}.xlsx', sheet_name = date_and_hour)

