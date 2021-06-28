from utils.WDriver import WDriver
from page_models.HomePage import HomePage
from page_models.AddNewComputerPage import AddNewComputerPage

#call driver
callWDriver = WDriver('chromedriver','http://computer-database.herokuapp.com/computers')
callWDriver.call_chrome_webdriver()

#home page
callHomePage = HomePage(callWDriver.driver)
callHomePage.validate_home_page_title()
callHomePage.click_add_new_computer()

#ADD A COMPUTER PAGE
callAddNewComputerPage = AddNewComputerPage(callWDriver.driver,'ABC','','')
callAddNewComputerPage.validate_add_new_computer_title_css()
#input values
callAddNewComputerPage.add_new_computer_name()
callAddNewComputerPage.add_new_computer_introduce_date()
callAddNewComputerPage.add_new_computer_discontinued_date()
callAddNewComputerPage.add_new_computer_company()
callAddNewComputerPage.create_computer()


assert(letter_in_string('Juan','J')) == 1 ,'Positive scenario with Uppercase Fails'
assert(letter_in_string('juan','j')) == 1 , 'Positive scenario with lowercase Fails'
assert(letter_in_string('Juanj','j')) == 2 , 'Positive scenario with Uppercase and lowercaseFails'
assert(letter_in_string('juan de dios',' ')) == 0, 'Negative scenario'
assert(letter_in_string('juan de dios','')) == 0, 'Negative scenario'
# assert "Done! Computer" in msg_add_success
# Done! Computer ABC has been created



