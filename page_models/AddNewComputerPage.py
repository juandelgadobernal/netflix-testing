from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from utils.Helpers import Helpers
from utils.Logs import Logs
import json
import random

class AddNewComputerPage():
    """AddNewComputerPage Class"""

    def __init__(self,driver, computer_name, introduced, discontinued):
        """
        This method Initialize the class
        :param driver: the webdriver [string]
        :param computer_name: Computer name[string]
        :param introduced: Introduced date [yyyy-mm-dd]
        :param discontinued: Discontinued date [yyyy-mm-dd]
        """
        self.driver = driver
        self.computer_name = computer_name
        self.introduced = introduced
        self.discontinued = discontinued

    def validate_add_new_computer_title_css(self):
        """
        This method validate and printthe "Add a computer" page title by CSS
        param list:
        :return:
        """
        self.add_new_computer_title = self.driver.find_element_by_css_selector("body:nth-child(2) section:nth-child(2) > h1:nth-child(1)").text
        if self.add_new_computer_title == 'Add a computer':
            print('ADD COMPUTER PAGE displayed - Title: {}'.format(self.add_new_computer_title))
        else:
            print('ADD COMPUTER PAGE not displayed as expected - Title: {}'.format(self.add_new_computer_title))

    def validate_add_new_computer_page_url(self):
        """
        This method print the add new computer page URL
        param list:
        :return:
        """
        print(self.driver.current_url)

    def add_new_computer_name(self):
        """
        This method input the "Computer name" by ID
        param list:
            self.computername
        :return:
        """
        self.driver.find_element_by_id('name').send_keys(self.computer_name)

    def add_new_computer_introduce_date(self):
        """
        This method input the "Introduced date" by ID
        param list command:
            self.introduced
        :return:
        """
        self.driver.find_element_by_id('introduced').send_keys(self.introduced)

    def add_new_computer_discontinued_date(self):
        """
        This method input the "Discontinued date" by ID
        param list command:
            self.discontinued
        :return:
        """
        self.driver.find_element_by_id('discontinued').send_keys(self.discontinued)

    def add_new_computer_introduce_date_random(self):
        """
        This method input the "Introduce date" randomly by ID
        param list command:
            callHelpers.past_date_random()
        :return:
        """
        callHelpers = Helpers()
        self.driver.find_element_by_id('introduced').send_keys(callHelpers.past_date_random())

    def add_new_computer_discontinued_date_random(self):
        """
        This method input the "Discontinued date" randomly by ID
        param list command:
            callHelpers.future_date_random()
        :return:
        """
        callHelpers = Helpers()
        self.driver.find_element_by_id('discontinued').send_keys(callHelpers.future_date_random())

    def add_new_computer_company_random(self):
        """
        This method input the "Company" randomly from the list by ID
        param list command:
            random.randint(Initial item, Total items)
        :return:
        """
        dropdown = Select(self.driver.find_element_by_id("company"))
        total_dp_items = (len(dropdown.options)) - 1
        # print(total_dp_items)
        dropdown.select_by_index(random.randint(1, total_dp_items))

    def create_computer(self):
        """
        This method click "Create this computer" to create the new computer
        param list command:
        :return: "True" is Test Pass or "False" if test Fail
        """
        self.driver.find_element_by_css_selector("input[value='Create this computer'][type='submit']").click()
        self.msg_add_success = self.driver.find_element_by_xpath("//*[contains(@class,'alert')]").text
        if "Done! Computer" in self.msg_add_success:
            print('PASS: Add computer {} has been created'.format(self.computer_name))
            return True
        else:
            print('FAIL: Add computer {} has NOT been created'.format(self.add_new_computer_title))
            return False

    def create_computer_data_missing(self):
        """
        This method click "Create this computer" to validate error message when data os missing
        Using CSS to identify the botton "Create this computer" and
        Using Xpath to identofy the "Err_msg"
        param list command:
        :return: "True" is Test Pass or "False" if test Fail
        """
        self.driver.find_element_by_css_selector("input[value='Create this computer'][type='submit']").click()
        self.err_msg_xp = self.driver.find_elements_by_xpath("//span[@class='help-inline']")
        print(len(self.err_msg_xp))

        for msg in self.err_msg_xp:
            if msg.text == "Required":
                self.err_msg = msg.text
                print('PASS: Error msg displayed - Error message(s): {}'.format(msg.text))
                return True
            else:
                print('FAIL: NO Error msg displayed- Error message(s): {}'.format(msg.text))
                return False

    def create_computer_data_incorrect_dates(self):
        """
        This method click "Create this computer" to validate error message when data date are incorrects format
        Using CSS to identify the botton "Create this computer" and
        Using Xpath to identofy the "Err_msg"
        param list command:
            self.err_msg_xp
        :return: "True" is Test Pass or "False" if test Fail
        """
        value = True
        self.driver.find_element_by_css_selector("input[value='Create this computer'][type='submit']").click()
        self.err_msg_xp = self.driver.find_elements_by_xpath("//span[@class='help-inline']")
        #print(len(err_msg_xp))

        for msg in self.err_msg_xp:
            if msg.text == "Date ('yyyy-MM-dd')":
                print('PASS: Error msg displayed - Error message(s): {}'.format(msg.text))
                self.err_msg = msg.text
                value =  True
            #elif msg.text == "Required":
            #    print('PASS: Error msg displayed - Error message(s): {}'.format(msg.text))
            #    value =  True
        return value

    def create_computer_cancel(self):
        """
        This method cancel the "Create this computer"
        :return:
        """
        self.driver.find_element_by_xpath("//a[text()='Cancel']").click()
        print('ADD COMPUTER PAGE displayed - Click "Cancel" button: Create computer Cancel {}'.format(''))

    def print_log_create_computer(self):
        """
        This method print long on a file log
        param list command:
            myName, msg_add_success, computer_name. discontinued
        :return:
        """
        self.myName = "TC_AddNewComputerPage"
        callLogs = Logs() #instancio la clase

        callLogs.write(self.myName)
        callLogs.write(self.msg_add_success)
        callLogs.write(self.computer_name)
        callLogs.write(self.introduced )
        callLogs.write(self.discontinued)
        callLogs.close()

    def print_log_create_computer_msg_errors(self):
        """
        This method print long on a file log
        param list command:
            myName, err_msg, computer_name. discontinued
        :return:
        """
        self.myName = "TC_AddNewComputerPage_Msg_Errors"
        callLogs = Logs()

        callLogs.write(self.myName)
        callLogs.write(self.err_msg)
        callLogs.write(self.computer_name)
        callLogs.write(self.introduced )
        callLogs.write(self.discontinued)
        callLogs.close()



