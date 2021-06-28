import unittest
import datetime
import pytz
import time
from utils.WDriver import WDriver
from utils.HelperJson import HelperJson
from page_models.HomePage import HomePage
from page_models.FoundComputerPage import FoundComputerPage
from page_models.DeleteComputerPage import DeleteComputerPage

class test_delete_new_computer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.start_ts_pst = ''

    def setUp(self):
        self.start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d %H:%M:%S.%f"'))

    def tearDown(self):
        end_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d %H:%M:%S.%f"'))
        print("Test start time: {}".format(self.start_ts_pst))
        print("Test end time  : {}".format(end_ts_pst))

    def test_delete_new_computer(self):

        print('*****************TC:test_delete_new_computer*******************')

        callHelperJson = HelperJson()
        dataComputer = callHelperJson.read('dataComputer.json')

        self.webdriver = dataComputer['webdriver']
        self.web_url = dataComputer['web_url']
        self.new_computer = dataComputer['new_computer']
        self.edit_new_computer_name = dataComputer['edit_new_computer']

        # call driver
        callWDriver = WDriver(self.webdriver, self.web_url)
        callWDriver.call_chrome_webdriver()

        # home page
        callHomePage = HomePage(callWDriver.driver, self.new_computer)
        callHomePage.validate_home_page_title()
        callHomePage.search_computer()

        # FOUND COMPUTER PAGE
        callFoundComputerPage = FoundComputerPage(callWDriver.driver, self.edit_new_computer_name, '', '')
        callFoundComputerPage.validate_found_computer_title_css()
        callFoundComputerPage.click_search_computer_name()

        callDeleteComputerPage = DeleteComputerPage(callWDriver.driver, self.edit_new_computer_name)
        callDeleteComputerPage.validate_delete_new_computer_title_css()
        #callDeleteComputerPage.delete_computer()

        val_delete_computer = callDeleteComputerPage.delete_computer()
        # assert is != to False, expecting True to check true of test value as computer edited
        assert val_delete_computer != False, 'Delete Computer Failed'

        callDeleteComputerPage.print_log_delete_computer()
        time.sleep(2)

        callWDriver.quit_chrome_webdriver()

if __name__ == '__main__':
    unittest.main()