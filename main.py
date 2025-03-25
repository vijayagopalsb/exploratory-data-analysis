# File: main.py
# Running the pipeline

# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns

# Import my libraries
from logging_config import logger
from handlers.understand_data import UnderstandDataset
from handlers.handle_missing_values import HandleMissingValues

# Load Dataset
dataframe = sns.load_dataset("titanic")

# Execute the EDA pipeline
logger.info("Starting EDA Pipeline ...") 
pipeline = UnderstandDataset(next_handler=HandleMissingValues( strategy="mean", next_handler=None))
dataframe = pipeline.handle(dataframe)

print(dataframe.head())

# EDA Pipeline Status
logger.info("EDA Pipeline Completed Successfully!")