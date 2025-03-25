# File: handlers/base_handler.py

# Step 2: Abstract Base Class
# All EDA steps inherit from this base class, uses a common interface

from logging_config import logger

class EDAHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler
        
    def handle(self, df):
        """ Process data and pass it to the next handler. """
        df = self.process(df)
        if self.next_handler:
            return self.next_handler.handle(df)
        return df
     
    def process(self, df):
        """ Abstract method for each step to implement. """
        raise NotImplementedError("Subclasses must implement 'process' method")