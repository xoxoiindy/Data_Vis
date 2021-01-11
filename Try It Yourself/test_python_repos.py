'''
17-3. Testing python_repos_visual.py: In python_repos_visual.py, we printed the value of
status_code to make sure the API call was successful. Write a program called
test_python_repos.py that uses unittest to assert that the value of status_code
is 200. Figure out some other assertions you can make—for example, that the
number of items returned is expected and that the total number of repositories
is greater than a certain amount.
'''

import unittest

from test_python_repos2 import get_repo, get_items, get_totals

# A TestCase  is the individual unit of testing.
# It checks for a specific response to a particular set of inputs.
# unittest provides a base class, TestCase, which may be used to create new test cases.

class RepoTestCase(unittest.TestCase):

    # This method tests the get_repo function from test_python_repos2
    def test1(self):
        # This stores the return value from the get_repo function in the variable status
        status = get_repo()
        # compares the value returned in the variable above called status and checks if it's equal to 200
        self.assertEqual(status, 200)
        print("Test1 checks if status is equal to 200")

    def test2(self):
        items = get_items()
        # test 2 then compares the value returned in the variable above called items and checks if it's equal to the 30 repositories
        self.assertEqual(items, 30)
        print("Test2 checks the total number of repositories")

    def test3(self):
        total = get_totals()
        # test32 then compares the value returned in the variable above called total and checks the number of repositories is greater
        self.assertGreater(total, 21)
        print("Test3 checks if the number of repositories is greater")


if __name__ == '__main__':
    unittest.main()

