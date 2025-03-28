# File: logging_config.py
# Step 1: Logging Configuration
# Define a centralized logger

import logging

# Custom filter to suppress the specific warning
class SuppressCategoricalWarningFilter(logging.Filter):
    def filter(self, record):
        return "Using categorical units to plot a list of strings" not in record.getMessage()

# Prevent warnings from being captured by the logging system
logging.captureWarnings(False)

# Configure Logging
logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s ->>> %(message)s",
                    handlers=[
                        logging.FileHandler("eda_pipeline.log"),  # Save logs to a file
                        logging.StreamHandler()  # Print logs to console
                    ])

# Apply the filter to the root logger
root_logger = logging.getLogger()
root_logger.addFilter(SuppressCategoricalWarningFilter())

# Define the module-level logger
logger = logging.getLogger(__name__)