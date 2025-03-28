# File: handlers/correlation.py

# Step 5: Performing correlation analysis...

# Import 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from handlers.base_handler import EDAHandler
from logging_config import logger

class CorrelationAnalysis(EDAHandler):

    def process(self, df):
        logger.info("Step 5: -->> Performing correlation analysis...")

        # Create a numeric copy of dataframe
        df_numeric = df.copy()

        # Convert categorical columns to numeric using encoding
        for col in df_numeric.select_dtypes(include=['object', 'category']).columns:
            if df_numeric[col].nunique() < 20:  # Encode categorical features (low cardinality)
                df_numeric[col] = df_numeric[col].astype('category').cat.codes
            else:
                logger.warning(f"Skipping {col}: Too many unique values, consider one-hot encoding.")

        # Convert all possible numbers in object columns
        df_numeric = df_numeric.apply(pd.to_numeric, errors='coerce')

        # Compute correlation matrix
        correlation_matrix = df_numeric.corr()

        if correlation_matrix.isnull().all().all():
            logger.warning("Correlation matrix contains only NaN values. Check data types.")
            return df

        # Plot correlation heatmap
        plt.figure(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Feature Correlation Matrix")
        plt.show()

        return df
