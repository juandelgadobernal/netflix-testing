# your intial test
import unittest
from suites.test_cases.test_add_new_computer import test_add_new_computer
from suites.test_cases.test_edit_new_computer import test_edit_new_computer
from suites.test_cases.test_delete_new_computer import test_delete_new_computer
from suites.test_cases.test_add_new_computer_req_data import test_add_new_computer_req_data
from suites.test_cases.test_add_new_computer_data_missing import test_add_new_computer_data_missing
from suites.test_cases.test_add_new_computer_data_incorrect import test_add_new_computer_data_incorrect
from suites.test_cases.test_computer_no_exist import test_computer_no_exist
from suites.test_cases.test_add_new_computer_cancel import test_add_new_computer_cancel
from suites.test_cases.test_computer_edit_delete_cancel import test_computer_edit_delete_cancel

# let MyTests and MyOtherTests be class that inherit from
# unittest.TestCase as in the examples above

tc1 = unittest.TestLoader().loadTestsFromTestCase(test_add_new_computer)
tc2 = unittest.TestLoader().loadTestsFromTestCase(test_edit_new_computer)
tc3 = unittest.TestLoader().loadTestsFromTestCase(test_delete_new_computer)
tc4 = unittest.TestLoader().loadTestsFromTestCase(test_add_new_computer_req_data)
tc5 = unittest.TestLoader().loadTestsFromTestCase(test_add_new_computer_data_missing)
tc6 = unittest.TestLoader().loadTestsFromTestCase(test_add_new_computer_data_incorrect)
tc7 = unittest.TestLoader().loadTestsFromTestCase(test_computer_no_exist)
tc8 = unittest.TestLoader().loadTestsFromTestCase(test_add_new_computer_cancel)
tc9 = unittest.TestLoader().loadTestsFromTestCase(test_computer_edit_delete_cancel)


#suite = unittest.TestLoader().loadTestsFromTestCase(MyOtherTests)
#all_tests = unittest.TestSuite([tc8])
all_tests = unittest.TestSuite([tc1,tc2,tc3,tc4,tc5,tc6,tc7,tc8,tc9])
print(all_tests)

unittest.TextTestRunner().run(all_tests)