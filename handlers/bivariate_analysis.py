# File: handlers/bivariate_analysis.py

# Step 3: Bivariate Analysis

# Import Libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import matplotlib
import logging

# Import App Libraries
from handlers.base_handler import EDAHandler
from logging_config import logger

class BivariateAnalysis(EDAHandler):
    def __init__(self, target_column, next_handler=None):
        super().__init__(next_handler)
        self.target_column = target_column
        
    def process(self, df):
        logger.info(f"Step 4: -->> Performing bivariate analysis with target '{self.target_column}'...")

        # Log library versions
        logger.info(f"Seaborn version: {sns.__version__}, Matplotlib version: {matplotlib.__version__}")

        # Ensure the target column exists
        if self.target_column not in df.columns:
            logger.error(f"Target column '{self.target_column}' not found in DataFrame.")
            raise ValueError(f"Target column '{self.target_column}' not found in DataFrame.")

        # Print target column data type
        logger.info(f"Original type of '{self.target_column}': {df[self.target_column].dtype}")

        # Select numeric columns for y-axis
        numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

        # Log sample of target column
        logger.info(f"Sample of '{self.target_column}': {df[self.target_column].head().tolist()}")

        # Suppress all warnings from Seaborn and Matplotlib
        warnings.filterwarnings("ignore", module="seaborn")
        warnings.filterwarnings("ignore", module="matplotlib")

        # Get the root logger
        root_logger = logging.getLogger()

        for col in numeric_columns:
            if col != self.target_column:
                try:
                    logger.info(f"Plotting {col} vs {self.target_column}...")

                    # Ensure Y-axis is numeric
                    df[col] = pd.to_numeric(df[col], errors="coerce")

                    # Log type just before plotting
                    logger.info(f"Type of '{self.target_column}' before plotting: {df[self.target_column].dtype}")

                    # Temporarily raise logging level to WARNING to suppress INFO messages
                    original_level = root_logger.level
                    root_logger.setLevel(logging.WARNING)
                    try:
                        sns.boxplot(x=df[self.target_column], y=df[col], order=[0, 1])
                        plt.title(f"{col} vs {self.target_column}")
                        plt.show()
                    finally:
                        # Restore original logging level
                        root_logger.setLevel(original_level)

                except Exception as e:
                    logger.error(f"Error plotting {col}: {e}")

        # Reset warnings (optional)
        warnings.resetwarnings()

        return df