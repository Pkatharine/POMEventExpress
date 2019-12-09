from locators import LocatorsLogIn
from selenium.webdriver.common.keys import Keys

from pages.BasePage import BasePage


class SignInPage(BasePage):

    def enter_credentials_and_enter(self, username, passwd):
        self.driver.find_element(*LocatorsLogIn.SIGN_IN_BUTTON).click()
        self.driver.find_element(*LocatorsLogIn.EMAIL_TEXT_FIELD).send_keys(username)
        pas = self.driver.find_element(*LocatorsLogIn.PASSWORD_TEXT_FIELD)
        pas.send_keys(passwd)
        pas.send_keys(Keys.ENTER)

    def get_user_name(self):
        return self.driver.find_element(*LocatorsLogIn.USERNAME_LABEL).text




