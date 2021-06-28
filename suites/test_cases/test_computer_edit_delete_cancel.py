import unittest
import datetime
import pytz
import time
from utils.WDriver import WDriver
from utils.HelperJson import HelperJson
from page_models.HomePage import HomePage
from page_models.FoundComputerPage import FoundComputerPage
from page_models.EditComputerPage import EditComputerPage

class test_computer_edit_delete_cancel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.start_ts_pst = ''

    def setUp(self):
        self.start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d %H:%M:%S.%f"'))

    def tearDown(self):
        end_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d %H:%M:%S.%f"'))
        print("Test start time: {}".format(self.start_ts_pst))
        print("Test end time  : {}".format(end_ts_pst))

    def test_edit_new_computer_cancel(self):

        print('*****************TC:test_edit_delete_new_computer_cancel*******************')

        callHelperJson = HelperJson()
        dataComputer = callHelperJson.read('dataComputer.json')

        self.webdriver = dataComputer['webdriver']
        self.web_url = dataComputer['web_url']
        self.new_computer = dataComputer['new_computer_cancel']
        self.edit_new_computer_name_cancel = dataComputer['new_computer_cancel_update']

        # call driver
        callWDriver = WDriver(self.webdriver, self.web_url)
        callWDriver.call_chrome_webdriver()

        # home page
        callHomePage = HomePage(callWDriver.driver, self.new_computer)
        callHomePage.validate_home_page_title()

        #HOME PAGE -Search
        callHomePage.search_computer()

        # FOUND COMPUTER PAGE
        callFoundComputerPage = FoundComputerPage(callWDriver.driver, self.new_computer, '', '')
        callFoundComputerPage.validate_found_computer_title_css()
        callFoundComputerPage.click_search_computer_name()

        callEditComputerPage = EditComputerPage(callWDriver.driver, self.new_computer, self.edit_new_computer_name_cancel, '', '')
        callEditComputerPage.validate_edit_new_computer_title_css()
        callEditComputerPage.edit_new_computer_name()
        callEditComputerPage.edit_new_computer_introduce_date_random()
        callEditComputerPage.edit_new_computer_discontinued_date_random()
        callEditComputerPage.edit_new_computer_company_random()

        # ADD A COMPUTER - CANCEL
        callEditComputerPage.edit_computer_cancel()

        # HOME PAGE
        val_home_page = callHomePage.validate_home_page_title()
        # assert is != to False, expecting True to check true of test value as computer created
        assert val_home_page != False, 'Edit Computer Cancel Failed'

        #VALIDATE NO UPDATED -------
        # HOME PAGE
        callHomePage = HomePage(callWDriver.driver, self.new_computer)
        callHomePage.validate_home_page_title()

        # HOME PAGE -Search
        callHomePage.search_computer()

        # FOUND COMPUTER PAGE
        callFoundComputerPage = FoundComputerPage(callWDriver.driver, self.new_computer, '', '')
        callFoundComputerPage.validate_found_computer_title_css()
        #callFoundComputerPage.click_search_computer_name()

        # SEARCH PAGE
        val_computer_name_no_updated = callFoundComputerPage.search_computer_name_text()
        # assert is != to False, expecting True to check true of test value as computer created
        assert val_computer_name_no_updated != False, 'Edit Computer Cancel Failed'

        #callEditComputerPage.print_log_edit_computer()
        time.sleep(2)

        callWDriver.quit_chrome_webdriver()

if __name__ == '__main__':
    unittest.main()