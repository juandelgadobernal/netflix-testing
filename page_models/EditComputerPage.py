#from AddNewComputerPage import AddNewComputerPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from utils.Helpers import Helpers
from utils.Logs import Logs
import random
import time

#class EditComputerPage(AddNewComputerPage):
class EditComputerPage():
    """EditComputerPage Class"""

    def __init__(self,driver, computer_name,edit_computer_name, edit_introduced, edit_discontinued):
        """
        This method Initialize the class
        :param driver: the webdriver [string]
        :param computer_name: Computer name[string]
        :param edit_computer_name: Update Computer name[string]
        :param edit_introduced: Introduced date [yyyy-mm-dd]
        :param edit_discontinued: Discontinued date [yyyy-mm-dd]
        """
        #super(EditComputerPage, self).__init__(self,driver, computer_name, introduced, discontinued)  #Father class
        self.driver = driver
        self.computer_name = computer_name
        self.edit_computer_name = edit_computer_name
        self.edit_introduced = edit_introduced
        self.edit_discontinued = edit_discontinued

    def validate_edit_new_computer_title_css(self):
        """
        This method validate and print the "Edit a computer" page title by CSS
        param list:
        :return:
        """
        self.edit_new_computer_title = self.driver.find_element_by_css_selector("body:nth-child(2) section:nth-child(2) > h1:nth-child(1)").text
        if self.edit_new_computer_title == 'Edit computer':
            print('EDIT COMPUTER PAGE displayed - Title: {}'.format(self.edit_new_computer_title))
        else:
            print('EDIT COMPUTER PAGE displayed not displayed as expected - Title: {}'.format(self.edit_new_computer_title))

    def edit_new_computer_name(self):
        """
        This method input the "Computer name" by ID on Edit computer page
        param list:
            self.edit_computer_name
        :return:
        """
        self.driver.find_element_by_id('name').clear()
        self.driver.find_element_by_id('name').send_keys(self.edit_computer_name)

    def edit_new_computer_introduce_date_random(self):
        """
        This method input the "Introduce date" randomly by ID on Edit computer page
        param list command:
            callHelpers.past_date_random()
        :return:
        """
        callHelpers = Helpers()
        self.driver.find_element_by_id('introduced').clear()
        time.sleep(1)
        self.driver.find_element_by_id('introduced').send_keys(callHelpers.past_date_random())

    def edit_new_computer_discontinued_date_random(self):
        """
        This method input the "Discontinued date" randomly by ID on Edit computer page
        param list command:
            callHelpers.future_date_random()
        :return:
        """
        callHelpers = Helpers()
        self.driver.find_element_by_id('discontinued').clear()
        time.sleep(1)
        self.driver.find_element_by_id('discontinued').send_keys(callHelpers.future_date_random())

    def edit_new_computer_company_random(self):
        """
        This method input the "Company" randomly by ID on Edit computer page
        param list command:
            callHelpers.future_date_random()
        :return:
        """
        dropdown = Select(self.driver.find_element_by_id("company"))
        total_dp_items = (len(dropdown.options)) - 1
        # print(total_dp_items)
        dropdown.select_by_index(random.randint(1, total_dp_items))

    def edit_computer(self):
        """
        This method click "Edit this computer" to edit an existing tnw computer
        param list command:
        :return: "True" is Test Pass or "False" if test Fail
        """
        self.driver.find_element_by_css_selector("input[value='Save this computer'][type='submit']").click()
        self.msg_edit_success = self.driver.find_element_by_xpath("//*[contains(@class,'alert')]").text
        if "has been updated" in self.msg_edit_success:
            print('PASS: Edited Computer {} has been updated to {}'.format(self.computer_name,self.edit_computer_name))
            return True
        else:
            print('FAIL: Edited Computer {} has been NOT updated'.format(self.edit_computer_name))
            return False

    def edit_computer_cancel(self):
        """
        This method cancel the "edit this computer" of delete propose
        :return:
        """
        self.driver.find_element_by_xpath("//a[text()='Cancel']").click()
        print('EDIT COMPUTER PAGE displayed - Click "Cancel" button: Edit computer Cancel {}'.format(''))


    def print_log_edit_computer(self):
        """
        This method print long on a file log
        param list command:
            myName, msg_edit_success, edit_computer_name,edit_discontinued
        :return:
        """
        self.myName = "TC_EditComputerPage"
        callLogs = Logs()

        callLogs.write(self.myName)
        callLogs.write(self.msg_edit_success)
        callLogs.write(self.edit_computer_name)
        callLogs.write(self.edit_introduced )
        callLogs.write(self.edit_discontinued)
        callLogs.close()
