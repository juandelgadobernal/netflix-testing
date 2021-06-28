import unittest
import datetime
import pytz
import time
from utils.WDriver import WDriver
from utils.HelperJson import HelperJson
from page_models.HomePage import HomePage
from page_models.FoundComputerPage import FoundComputerPage
from page_models.EditComputerPage import EditComputerPage

class test_computer_no_exist(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.start_ts_pst = ''

    def setUp(self):
        self.start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d %H:%M:%S.%f"'))

    def tearDown(self):
        end_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d %H:%M:%S.%f"'))
        print("Test start time: {}".format(self.start_ts_pst))
        print("Test end time  : {}".format(end_ts_pst))

    def test_computer_no_exist(self):

        print('*****************TC:test_computer_no_existr*******************')

        callHelperJson = HelperJson()
        dataComputer = callHelperJson.read('dataComputer.json')

        self.webdriver = dataComputer['webdriver']
        self.web_url = dataComputer['web_url']
        self.new_computer = dataComputer['new_computer_no_exist']

        # call driver
        callWDriver = WDriver(self.webdriver, self.web_url)
        callWDriver.call_chrome_webdriver()

        # home page
        callHomePage = HomePage(callWDriver.driver, self.new_computer)
        callHomePage.validate_home_page_title()
        callHomePage.search_computer()
        #time.sleep(2)

        # FOUND COMPUTER PAGE
        callFoundComputerPage = FoundComputerPage(callWDriver.driver, self.new_computer, '', '')
        val_no_computer = callFoundComputerPage.validate_found_no_computer_title_css()
        # assert is != to False, expecting True to check true of test value as computer edited
        assert val_no_computer != False, 'Search Computer exist then Failed'

        #callEditComputerPage.print_log_edit_computer()
        #time.sleep(2)

        callWDriver.quit_chrome_webdriver()

if __name__ == '__main__':
    unittest.main()