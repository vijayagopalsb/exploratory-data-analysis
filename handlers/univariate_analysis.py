# File: handlers/univariate_analysis.py

# Import Libraries
import matplotlib.pyplot as plt
from handlers.base_handler import EDAHandler
# Import App Libraries
from logging_config import logger

class UnivariateAnalysis(EDAHandler):
    
    def process(self, df):
        
        logger.info("Step 3: -->> Performimg Univariate Analysis ...")
        
        df.hist(figsize=(10,6), bins=20) 
        plt.show()
        
        return df
    