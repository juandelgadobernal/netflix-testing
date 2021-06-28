
from utils.Logs import Logs

class DeleteComputerPage():
    """DeleteComputerPage Class"""

    def __init__(self,driver, computer_name,):
        """
        This method Initialize the class
        :param driver: the webdriver [string]
        :param computer_name: Computer name[string]
        """
        #super(EditComputerPage, self).__init__(self,driver, computer_name, introduced, discontinued)  #Father class
        self.driver = driver
        self.computer_name = computer_name

    def validate_delete_new_computer_title_css(self):
        """
        This method validate and print the "Delete a computer" page title by CSS
        param list:
        :return:
        """
        self.edit_new_computer_title = self.driver.find_element_by_css_selector("body:nth-child(2) section:nth-child(2) > h1:nth-child(1)").text
        if self.edit_new_computer_title == 'Edit computer':
            print('DELETE PAGE displayed - Title page displayed: {}'.format(self.edit_new_computer_title))
        else:
            print('DELETE PAGE displayed - Title page not displayed as expected: {}'.format(self.edit_new_computer_title))

    def delete_computer(self):
        """
        This method validate when a computer is deleted
        param list command:
        :return: "True" is Test Pass or "False" if test Fail
        """
        self.driver.find_element_by_css_selector("input[value='Delete this computer'][type='submit']").click()
        self.msg_delete_success = self.driver.find_element_by_xpath("//*[contains(@class,'alert')]").text
        if "Computer has been deleted" in self.msg_delete_success:
            print('HOME PAGE - Computer {} has been deleted'.format(self.computer_name))
            return True
        else:
            print('HOME PAGE - Computer {} has NOT been deleted'.format(self.computer_name))
            return False

    def print_log_delete_computer(self):
        """
        This method print long on a file log
        param list command:
            myName, msg_delete_success, computer_name
        :return:
        """
        self.myName = "TC_DeleteComputerPage"
        callLogs = Logs() #instancio la clase

        callLogs.write(self.myName)
        callLogs.write(self.msg_delete_success)
        callLogs.write(self.computer_name)
        #callLogs.write(self.edit_introduced )
        #callLogs.write(self.edit_discontinued)
        callLogs.close()