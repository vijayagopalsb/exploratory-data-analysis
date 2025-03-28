# File: handlers/understand_data.py

# Step 3: Understanding the datset

import pandas as pd

# Import my libraries
from handlers.base_handler import EDAHandler
from logging_config import logger

class UnderstandDataset(EDAHandler):
    
    def process(self, dataframe):
        logger.info("Step 1: -->> Understanding the dataset ...")

        logger.info("\nDisplay Features of Dataset:")
        logger.info(dataframe.info())

        logger.info("\nSummary Statistics:")
        logger.info(dataframe.describe(include="all"))

        logger.info("\nMissing Values:")
        logger.info(dataframe.isnull().sum())

        return dataframe  # Pass to next handler
