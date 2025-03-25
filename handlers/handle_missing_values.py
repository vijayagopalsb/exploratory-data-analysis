# File: handlers/handle_missing_values.py

# Step 3: Handling Missing Values

# Import Libraries

import pandas as pd

# Import my Libraries
from handlers.base_handler import EDAHandler
from logging_config import logger

class HandleMissingValues(EDAHandler):
    def __init__(self, strategy="mean", next_handler=None):
        super().__init__(next_handler)
        self.strategy = strategy
        
    def process(self, dataframe):
        logger.info(f"Step 2: Handling missing values using {self.strategy} strategy ...")
        
        for col in dataframe.columns:
            if dataframe[col].isnull().sum() > 0:
                if dataframe[col].dtype == "object" or dataframe[col].dtype.name == "category":
                    # Fill categorical data with mode
                    dataframe[col] = dataframe[col].fillna(dataframe[col].mode()[0])
                else:
                    if self.strategy == "mean":
                        dataframe[col] = dataframe[col].fillna(dataframe[col].mean())
                    elif self.strategy == "median":
                        dataframe[col] = dataframe[col].fillna(dataframe[col].median())
                    
        return dataframe
                
    
