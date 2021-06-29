# Netflix Assessment
Create a series of manual test cases that cover the CRUD operation plus the edge cases.Make sure you give detailed instructions for each test case (pre conditions, steps, expectedresults). You may use any format you want

The app under test is [Computer database](http://computer-database.herokuapp.com/computers/)

## Structure of netflix-testing
The following section contains an explanation of the different folders that compose the project, and the content of each one of them.

## Test Automation Framework Design 
Page Object Model (POM) as a design pattern where the web pages are represented as classes, and the various elements on the page are defined as variables on the class. Also a Json file to parameterization the test scripts in order to pass multiple data to the application at runtime. Besides "asserts" for validate the test scripts.

## Languages and Libraries
    * Python 3.6
    * driver Selenium webdriver (Chrome)
    * lib unnitest, json
   

## Project Folder Directory

* **browser_driver:**
This folder store the Chrome WebDriver for our automated testing of webapps

* **page_models:**
This folder contains our design pattern the Page Object Model (also known as POM) in Selenium that creates an object repository for storing all web elements. 
This Page Object Model considers each web page of the application under test as a class file.

    * AddNewComputerPage
    * EditComputerPage
    * DeleteComputerPage
    * FoundComputerPage
    * HomePage

* **suites:**
The suite folder contains the subfolder with the following:
 
    * **log**
the folder allocate a file report created on each execution per day with all the actions made

    * **regression**
The unnittest py file to run all our test cases

    * **test cases**
the folder with all the test cases

    * **test data**
the folder contain the dataComputer.json with all the input values per each test case

* **utils:**
the folder contain classes to help us with our execution for commun action or validations

## Quality Approach & strategy
### CRUD Operation Test_Cases

| ID. |  CRUD   | Priority |  Manual TC (Rest method)                        | Method   | Automated | Comments | 
|:----|:--------|:--------:|:------------------------------------------------|:--------:|:---------:|:---------|
|E2E  | All     | High     | Add new computer then update then delete        | Positive | Yes       |          |
|C01  | Create  | High     | Add new computer all optional and required data | Positive | Yes       |          |
|C02  | Create  | High     | Add new computer only required data             | Positive | Yes       |          |
|C03  | Create  | Medium   | Add new computer with required data missing     | Negative | Yes       |          |  
|C04  | Create  | Low      | Add new computer with invalid data              | Negative | Yes       |          | 
|C05  | Create  | Low      | Add new computer cancel.                        | Positive | Yes       |          |
|R01  | Read    | High     | Read when computer exist                        | Positive | Yes       |          | 
|R02  | Read    | High     | Read when computer doesn't exist                | Negative | Yes       |          | 
|U01  | Update  | High     | Update existing computer                        | Positive | Yes       |          | 
|U02  | Update  | Medium   | Update non-existing computer                    | Negative | Yes       |          | 
|U03  | Update  | Medium   | Update deleted computer                         | Negative | Yes       |          |
|U04  | Update  | Low      | Update existing computer cancel                 | Positive | Yes       |          |
|U05  | Update  | Low      | Update existing computer then update again      | Negative | No        | WIP      | 
|D01  | Delete  | High     | Delete new computer                             | Positive | Yes       |          | 
|D02  | Delete  | Medium   | Delete non-existing computer                    | Negative | Yes       |          | 
|D03  | Delete  | Low      | Delete new computer cancel                      | Positive | Yes       |          | 
|D04  | Delete  | Low      | Delete new computer with dependencies           | Positive | No        | TBD      | 
|D05  | Delete  | Low      | Delete after delete                             | Positive | No        | TBD      | 

### CRUD Operation Test_Cases - Traxability Matrix

| TC no. | TC Name.                             | E2E | C01 | C02 | C03 | C04 | C05 | R01 | R02 | U01 | U02 | U03 | U04 | U05 | D01 | D02 | D03 | D04 | D05 | 
|:------:|:-------------------------------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| TC1    | test_add_new_computer                | X   |  X  |     |     |     |     |  X  |     |     |     |     |     |     |     |     |     |     |     |   
| TC2    | test_edit_new_computer               | X   |     |     |     |     |     |  X  |     |  X  |     |     |     |     |     |     |     |     |     |
| TC3    | test_delete_new_computer             | X   |     |     |     |     |     |     |     |     |     |     |     |     |  X  |     |     |     |     |
| TC4    | test_add_new_computer_req_data       | X   |     |  X  |     |     |     |  X  |     |     |     |     |     |     |     |     |     |     |     |
| TC5    | test_add_new_computer_data_missing   |     |     |     |  X  |     |     |  X  |     |     |     |     |     |     |     |     |     |     |     |
| TC6    | test_add_new_computer_data_incorrect |     |     |     |     |  X  |     |  X  |     |     |     |     |     |     |     |     |     |     |     |
| TC7    | test_computer_no_exist               |     |     |     |     |     |     |     |  X  |     |  X  |  X  |     |     |     |     |     |     |     |
| TC8    | test_add_new_computer_cancel         |     |     |     |     |     |  X  |     |     |     |  X  |     |  X  |     |     |  X  |     |     |     |
| TC9    | test_computer_edit_delete_cancel     |     |     |     |     |     |     |  X  |     |  X  |     |     |     |     |     |     |  X  |     |     |

## Requirements
* **Selenium webdriver:**
Using Chromedriver from usr/local/bin but please you can download from browser_driver folder
Reference for install [Chrome driver](https://chromedriver.chromium.org/)

* **Absolute paths:**
Absolute paths used on Utils Folder for the class HelperJson and Logs

## Demo
* **Prefered use :**
To run all of the tests from the regression suite folder that contains all the list of test scripts (classes), we are using a TestLoader's to get a TestSuite of tests for each class, and then create a single combined TestSuite from a list containing all of those suites to use with run:

```
regression.py as a unnittest
```
## Notes
* **To Do/In Progresss :**
Implement HTMLReports, the multi-run in different browsers in parallel (even consider the options as Browserstack), Besides the code best practies and refactor after a code review.

