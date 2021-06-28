
class FoundComputerPage():
    """FoundComputerPage Class"""

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

    def validate_found_computer_title_css(self):
        """
        This method validate and print the "Found a computer" page title by CSS
        param list:
        :return:
        """
        self.found_new_computer_title = self.driver.find_element_by_css_selector("body:nth-child(2) section:nth-child(2) > h1:nth-child(1)").text
        if 'computer found' in self.found_new_computer_title:
            print('FOUND COMPUTER PAGE displayed - Title: {}'.format(self.found_new_computer_title))
        else:
            print('FOUND COMPUTER PAGE not displayed as expected - Title: {}'.format(self.found_new_computer_title))

    def validate_found_no_computer_title_css(self):
        """
        This method validate when a computer is not found
        param list command:
        :return: "True" is Test Pass or "False" if test Fail
        """
        self.found_no_computer_title = self.driver.find_element_by_css_selector("body:nth-child(2) section:nth-child(2) > h1:nth-child(1)").text
        if 'No computers found' in self.found_no_computer_title:
            print('NO FOUND COMPUTER PAGE displayed - Title: {}'.format(self.found_no_computer_title))
            return True
        else:
            print('FOUND COMPUTER PAGE not displayed as expected - Title: {}'.format(self.found_no_computer_title))
            return False

    def click_search_computer_name(self):
        """
        This method click on the cmputer name found by linl text
        param list:
        :return:
        """
        self.driver.find_element_by_link_text(self.computer_name).click()

    def search_computer_name_text(self):
        """
        This method click on the cmputer name found by linl text
        param list:
        :return:
        """
        #print('nuevo valor',self.driver.find_element_by_link_text(self.computer_name).text)
        self.computer_no_updated = self.driver.find_element_by_link_text(self.computer_name).text
        if self.computer_name == self.computer_no_updated:
            print('PASS: Computer NO UPDATED: {}'.format(self.computer_name))
            return True
        else:
            print('FAIL: Computer UPDATED: {}'.format(self.computer_name))
            return False
