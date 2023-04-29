import pandas as pd
from datetime import datetime

class DataFrameManager:
    def __init__(self):
        self.dataframe = pd.DataFrame()

    def append(self, data_dicts):
        for data_dict in data_dicts:
            data_dict = pd.DataFrame(data_dict, index = range(1))
            if(self.dataframe.empty):
                self.dataframe = data_dict
            else:
                self.dataframe = pd.concat([self.dataframe, data_dict], axis = 0, ignore_index = True)
    
    def export(self):
        self.dataframe.to_excel('featured_products.xlsx', sheet_name = str(datetime.today().date()))

