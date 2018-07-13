import unittest
from lib.ui.login_page import LoginPage
from lib.utils import create_driver

class TestLoginU18756(unittest.TestCase):
    def setUp(self):
        self.driver = create_driver.get_driver_instance()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_invalid_tc154321(self):
        # 1 go to login page
        self.login_page.wait_for_login_page_to_load()
        #2 enter valid username
        self.login_page.get_username_textbox().send_keys('admin')
        #enter invalid password
        self.login_page.get_password_textbox().send_keys('Invalid')
        #4 click on login button
        self.login_page.get_login_button().click()

        actual_error_msg = self.login_page.get_login_error_msg().text
        expected_error_msg = 'Username or Password is invalid. Please try again.'
        assert actual_error_msg == expected_error_msg





























