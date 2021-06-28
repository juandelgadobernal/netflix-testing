from utils.WDriver import WDriver
from page_models.HomePage import HomePage
from page_models.FoundComputerPage import FoundComputerPage
from page_models.DeleteComputerPage import DeleteComputerPage

def delete_new_computer(webdriver,web_url,new_computer_name):

    #call driver
    callWDriver = WDriver(webdriver,web_url)
    callWDriver.call_chrome_webdriver()

    #home page
    callHomePage = HomePage(callWDriver.driver,new_computer_name)
    callHomePage.validate_home_page_title()
    callHomePage.search_computer()

    #EFOUN COMPUTER
    callFoundComputerPage = FoundComputerPage(callWDriver.driver,new_computer_name,'','')
    callFoundComputerPage.validate_found_computer_title_css()
    callFoundComputerPage.click_search_computer_name()

    callDeleteComputerPage = DeleteComputerPage(callWDriver.driver,new_computer_name)
    callDeleteComputerPage.validate_delete_new_computer_title_css()
    callDeleteComputerPage.delete_computer()



if __name__ == '__main__':
    webdriver = "chromedriver"
    web_url = "http://computer-database.herokuapp.com/computers"
    new_computer_name = "ABC"
    #edit_new_computer_name = "ABC_Update"
    delete_new_computer(webdriver,web_url,new_computer_name)