from locators import LocatorsHomePage
# from pages.BasePage import BasePage
from pages.BasePage import BasePage


class HomePage(BasePage):

    def click_profile_settings(self):
        self.driver.find_element(*LocatorsHomePage.SETTINGS_BUTTON).click()
        # self.browser.click_element(self.locators.SETTINGS_BUTTON)

