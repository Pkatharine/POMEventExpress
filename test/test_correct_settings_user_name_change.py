import unittest
from pages.LogInPage import SignInPage
from pages.HomePage import HomePage
from pages.SettingsPage import SettingsPage
from selenium import webdriver
from test_data import user_data


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        cls.driver.get("http://localhost:53326/")
        cls.driver.implicitly_wait(10)

    def test_open_event_express(self):
        sign_in_page = SignInPage(self.driver)
        sign_in_page.enter_credentials_and_enter(user_data.EMAIL_LOG_IN, user_data.PASSWORD_LOG_IN)
        self.assertEqual(sign_in_page.get_user_name(), "UserTest")

    def test_open_settings_page(self):
        home_page = HomePage(self.driver)
        home_page.click_profile_settings()

    def test_verify_changing_username(self):
        settings_page = SettingsPage(self.driver)
        settings_page.click_user_name_settings()
        self.assertEqual(settings_page.change_user_name_text("1"), "Username is changed")


    @classmethod
    def tearDownClass(cls):
        cls.driver.refresh()
        settings_page2 = SettingsPage(cls.driver)
        settings_page2.click_user_name_settings()
        settings_page2.change_user_name_text("UserTest")
        cls.driver.close()
        pass


if __name__ == '__main__':
    unittest.main()