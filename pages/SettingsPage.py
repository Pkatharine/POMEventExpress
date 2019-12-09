from selenium.webdriver.common.keys import Keys

from locators import LocatorsSettings
from pages.BasePage import BasePage


class SettingsPage(BasePage):

    def click_user_name_settings(self):
        self.driver.find_elements(*LocatorsSettings.CHANGE_USERNAME)[1].click()
        # self.browser.click_element(self.locators.CHANGE_USERNAME)

    def change_user_name_text(self, value):
        c = self.driver.find_element(*LocatorsSettings.CHANGE_USERNAME_INPUT)
        c.send_keys(value)
        # self.browser.send_keys(self.locators.CHANGE_USERNAME_INPUT, value)
        c.send_keys(Keys.ENTER)
        # self.browser.send_keys(Keys.ENTER)
        return self.driver.find_element(*LocatorsSettings.SUCCESS_NOTIFY).text
        # text = self.browser.get_text_of_element(self.locators.SUCCESS_NOTIFY)
        # return text
