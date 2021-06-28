import datetime
import pytz
from datetime import datetime

class Logs:
    """Logs Class"""

    def __init__(self):
        """
        Initialize the class and the attributes of the class
        """
        #folder = "../log/" #unittest
        folder ="/Users/juandelgado/PycharmProjects/netflix-testing/suites/log/"
        today = datetime.now().strftime("%m-%d-%y")
        self.out = open (folder+today+".txt","a") #la a significa append

    def write(self,text):
        """
        This method write in the log file
        :param text: each class write their data
        :return:
        """
        self.timestamp_log = str(datetime.now().strftime("%m-%d %H:%M:%S.%f"))
        self.timestamp_log = self.timestamp_log + ": "
        self.out.write(self.timestamp_log)
        self.out.write(text)
        self.out.write("\n")

    def close(self):
        """
        This method close the log file
        :return:
        """
        self.out.close()