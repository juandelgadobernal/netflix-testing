# Netflix Assessment
Create a series of manual test cases that cover the CRUD operation plus the edge cases.Make sure you give detailed instructions for each test case (pre conditions, steps, expectedresults). You may use any format you want

The app under test is [Computer database](http://computer-database.herokuapp.com/computers/)

## Structure
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

    * **report**
not used for now

    * **test cases**
the folder with all the test cases

    * **test data**
the folder contain the dataComputer.json with all the input values per each test case

* **utils:**
the folder contain classes to help us with our execution for commun action or validations

## Quality Approach & strategy
### test_cases - Traxability Matrix


| No.   | TC Description and name                 | CREATE  | READ    | UPDATE   | DELETE |
|:-----:|:----------------------------------------|:-------:|:-------:|:--------:|:------:|
| 1     | test_add_new_computer                   |    X    |   X     |          |        |
| 2     | test_edit_new_computer                  |         |   X     |    X     |        |
| 3     | test_delete_new_computer                |         |   X     |          |   X    |
| 4     | test_add_new_computer_req_data          |    X    |   X     |          |        |
| 5     | test_add_new_computer_data_missing      |    X    |   X     |          |        |
| 6     | test_add_new_computer_data_incorrect    |         |   X     |          |        |
| 7     | test_computer_no_exist                  |         |   X     |    X     |   X    |
| 8     | test_add_new_computer_cancel            |    X    |   X     |          |        |
| 9     | test_computer_edit_delete_cancel        |         |   X     |    X     |   X    |


## Demo
To run all of the tests from the regression suite folder that contains all the list of test scripts (classes), we are using a TestLoader's to get a TestSuite of tests for each class, and then create a single combined TestSuite from a list containing all of those suites to use with run:

```
regression.py as a unnittest
```
