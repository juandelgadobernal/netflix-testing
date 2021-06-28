import random
from datetime import datetime, timedelta
import time

class Helpers:
    """Helper Class"""

    def __init__(self):
        """
        Initialize the class and the attributes of the class
        Pre-condition:
        param str web_driver: web driver to use
        param str url: url of the web page to test
        returns:
        """

    def past_date_random(self):
        """
        This method generate a past date in format yyy-mm-dd
        :return: past date
        """
        random_past_date = random.randint(365, 3650)
        past_date = (datetime.now() - timedelta(days = random_past_date)).strftime("%Y-%m-%d")
        #print(past_date)
        return past_date

    def future_date_random(self):
        """
        This method generate a future date in format yyy-mm-dd
        :return: future_date
        """
        random_future_date = random.randint(120, 1095)
        future_date = (datetime.now() + timedelta(days = random_future_date)).strftime("%Y-%m-%d")
        #print(future_date)
        return future_date