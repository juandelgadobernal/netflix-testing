from utils.WDriver import WDriver
from page_models.HomePage import HomePage
from page_models.AddNewComputerPage import AddNewComputerPage

def add_new_computer(webdriver,web_url,new_computer):

    #call driver
    callWDriver = WDriver(webdriver,web_url)
    callWDriver.call_chrome_webdriver()

    #home page
    callHomePage = HomePage(callWDriver.driver,'')
    callHomePage.validate_home_page_title()
    callHomePage.click_add_new_computer()

    #ADD A COMPUTER PAGE
    callAddNewComputerPage = AddNewComputerPage(callWDriver.driver,new_computer,'','')
    callAddNewComputerPage.validate_add_new_computer_title_css()
    #input values
    callAddNewComputerPage.add_new_computer_name()
    callAddNewComputerPage.add_new_computer_introduce_date_random()
    callAddNewComputerPage.add_new_computer_discontinued_date_random()
    callAddNewComputerPage.add_new_computer_company_random ()
    callAddNewComputerPage.create_computer()
    callAddNewComputerPage.print_log_create_computer()

if __name__ == '__main__':
    webdriver = "chromedriver"
    web_url = "http://computer-database.herokuapp.com/computers"
    new_computer = "ABC"
    add_new_computer(webdriver,web_url,new_computer)

"""
    assert(add_new_computer(webdriver,web_url,new_computer)) == False ,'Positive scenario with correct Name'
    assert(letter_in_string('juan','j')) == 1 , 'Positive scenario with lowercase Fails'
    assert(letter_in_string('Juanj','j')) == 2 , 'Positive scenario with Uppercase and lowercaseFails'
    assert(letter_in_string('juan de dios',' ')) == 0, 'Negative scenario'
    assert(letter_in_string('juan de dios','')) == 0, 'Negative scenario'
    # assert "Done! Computer" in msg_add_success
    # Done! Computer ABC has been created
"""