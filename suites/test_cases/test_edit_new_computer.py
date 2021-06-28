import unittest
import datetime
import pytz
import time
from utils.WDriver import WDriver
from utils.HelperJson import HelperJson
from page_models.HomePage import HomePage
from page_models.FoundComputerPage import FoundComputerPage
from page_models.EditComputerPage import EditComputerPage

class test_edit_new_computer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.start_ts_pst = ''

    def setUp(self):
        self.start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d %H:%M:%S.%f"'))

    def tearDown(self):
        end_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d %H:%M:%S.%f"'))
        print("Test start time: {}".format(self.start_ts_pst))
        print("Test end time  : {}".format(end_ts_pst))

    def test_edit_new_computer(self):

        print('*****************TC:test_edit_new_computer*******************')

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
        callFoundComputerPage = FoundComputerPage(callWDriver.driver, self.new_computer, '', '')
        callFoundComputerPage.validate_found_computer_title_css()
        callFoundComputerPage.click_search_computer_name()

        callEditComputerPage = EditComputerPage(callWDriver.driver, self.new_computer, self.edit_new_computer_name, '', '')
        callEditComputerPage.validate_edit_new_computer_title_css()
        callEditComputerPage.edit_new_computer_name()
        callEditComputerPage.edit_new_computer_introduce_date_random()
        callEditComputerPage.edit_new_computer_discontinued_date_random()
        callEditComputerPage.edit_new_computer_company_random()

        val_edit_computer = callEditComputerPage.edit_computer()
        # assert is != to False, expecting True to check true of test value as computer edited
        assert val_edit_computer != False, 'Edited Computer Failed'

        callEditComputerPage.print_log_edit_computer()
        time.sleep(2)

        callWDriver.quit_chrome_webdriver()

if __name__ == '__main__':
    unittest.main()