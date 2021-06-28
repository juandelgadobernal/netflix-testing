import unittest
import datetime
import pytz
import time
from utils.WDriver import WDriver
from utils.HelperJson import HelperJson
from page_models.HomePage import HomePage
from page_models.FoundComputerPage import FoundComputerPage
from page_models.AddNewComputerPage import AddNewComputerPage

class test_add_new_computer_cancel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.start_ts_pst = ''

    def setUp(self):
        self.start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d %H:%M:%S.%f"'))

    def tearDown(self):
        end_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d %H:%M:%S.%f"'))
        print("Test start time: {}".format(self.start_ts_pst))
        print("Test end time  : {}".format(end_ts_pst))

    def test_add_new_computer_req_data(self):

        print('*****************TC:test_add_new_computer_cancel*******************')

        callHelperJson = HelperJson()
        dataComputer = callHelperJson.read('dataComputer.json')

        self.webdriver = dataComputer['webdriver']
        self.web_url = dataComputer['web_url']
        self.new_computer = dataComputer['new_computer_not_added']

        # call driver
        callWDriver = WDriver(self.webdriver, self.web_url)
        callWDriver.call_chrome_webdriver()

        # HOME PAGE
        #callHomePage = HomePage(callWDriver.driver, '')
        callHomePage = HomePage(callWDriver.driver, self.new_computer)
        callHomePage.validate_home_page_title()
        callHomePage.click_add_new_computer()

        # ADD A COMPUTER PAGE
        callAddNewComputerPage = AddNewComputerPage(callWDriver.driver, self.new_computer, '', '')
        callAddNewComputerPage.validate_add_new_computer_title_css()

        # input values
        callAddNewComputerPage.add_new_computer_name()
        callAddNewComputerPage.add_new_computer_introduce_date_random()
        callAddNewComputerPage.add_new_computer_discontinued_date_random()
        callAddNewComputerPage.add_new_computer_company_random()

        # ADD A COMPUTER - CANCEL
        callAddNewComputerPage.create_computer_cancel()

        # HOME PAGE
        val_home_page = callHomePage.validate_home_page_title()
        #assert is != to False, expecting True to check true of test value as computer created
        assert val_home_page != False, 'Create Computer Cancel Failed'

        #VALIDATE NO ADDED -------
        # HOME PAGE
        callHomePage = HomePage(callWDriver.driver, self.new_computer)

        # HOME PAGE -Search
        callHomePage.search_computer()
        #time.sleep(2)

        # FOUND COMPUTER PAGE
        callFoundComputerPage = FoundComputerPage(callWDriver.driver, self.new_computer, '', '')
        val_no_computer = callFoundComputerPage.validate_found_no_computer_title_css()
        # assert is != to False, expecting True to check true of test value as computer edited
        assert val_no_computer != False, 'Search Computer exist then Failed'

        #callAddNewComputerPage.print_log_create_computer()
        time.sleep(2)

        callWDriver.quit_chrome_webdriver()

if __name__ == '__main__':
    unittest.main()
