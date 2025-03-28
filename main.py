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
from handlers.univariate_analysis import UnivariateAnalysis
from handlers.bivariate_analysis import BivariateAnalysis
from handlers.correlation_analysis import CorrelationAnalysis
# Load Dataset
dataframe = sns.load_dataset("titanic")

# Execute the EDA pipeline
logger.info("Starting EDA Pipeline ...") 


pipeline = UnderstandDataset(
    next_handler=HandleMissingValues(
        next_handler=UnivariateAnalysis(
            next_handler=BivariateAnalysis(
                next_handler=CorrelationAnalysis(),
                target_column="survived"
            )
        ),
        strategy="mean"
    )
)

dataframe = pipeline.handle(dataframe)

# EDA Pipeline Status
logger.info("EDA Pipeline Completed Successfully!")