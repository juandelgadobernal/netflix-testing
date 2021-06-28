from utils.WDriver import WDriver

class HomePage():
    """HomePage Class"""

    def __init__(self,driver,new_computer):
        """
        This method Initialize the class
        :param driver: the webdriver [string]
        :param new_computer: Computer name[string]
        """
        self.driver = driver
        self.new_computer = new_computer

    def validate_home_page_title(self):
        """
        This method validate and print the "Home" page title by CSS
        param list:
        :return:
        """
        self.home_page_title = self.driver.find_element_by_css_selector("body:nth-child(2) section:nth-child(2) > h1:nth-child(1)").text
        if "computers found" in self.home_page_title:
            print('HOME PAGE - Title page displayed: {}'.format(self.home_page_title))
            return True
        else:
            print('HOME PAGE - Title page not displayed as expected: {}'.format(self.home_page_title))
            return False

    def click_add_new_computer(self):
        """
        This method click on the add new computer name found by ID
        param list:
        :return:
        """
        self.driver.find_element_by_id('add').click()

    def validate_home_page_url(self):
        """
        This method print current url
        param list:
        :return:
        """
        print(self.driver.current_url)

    def search_computer(self):
        """
        This method click on search submit found by click
        param list:
        :return:
        """
        self.driver.find_element_by_id('searchbox').send_keys(self.new_computer)
        self.driver.find_element_by_id('searchsubmit').click()


