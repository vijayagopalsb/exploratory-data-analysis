# File: handlers/understand_data.py

# Step 3: Understanding the datset

import pandas as pd

# Import my libraries
from handlers.base_handler import EDAHandler
from logging_config import logger

class UnderstandDataset(EDAHandler):
    
    def process(self, dataframe):
        logger.info("Step 1: Understanding the datset ...")
        
        print("\nDisplay Features of Dataset:")
        print(dataframe.info())
        print("\nSummary Statistics:")
        print(dataframe.describe(include= "all"))
        print("\nMissing Values:")
        print(dataframe.isnull().sum())
        
        return dataframe # Pass to next handler