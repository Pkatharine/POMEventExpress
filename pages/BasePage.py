# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class BasePage(object):
#     def __init__(self, driver, default_timeout=10):
#         self.driver = driver
#         self.default_timeout = default_timeout
#
#     def get_element(self, locator):
#         return self.driver.find_element(*locator)
#
#     def get_elements(self, locator):
#         WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_all_elements_located(locator))
#         return self.driver.find_elements(*locator)
#
#     def click_element(self, locator, elem_number=0):
#         WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable(locator))
#         elements = self.get_elements(locator)
#         elements[elem_number].click()
#
#     def send_keys(self, locator, keys, text_value='default'):
#         WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(locator))
#         elements = self.get_elements(locator)
#         if text_value == 'default':
#             elements[0].send_keys(keys)
#         else:
#             for element in elements:
#                 if element.text == text_value:
#                     element.send_keys(keys)
#
#     def get_text_of_element(self, locator):
#         WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(locator))
#         return self.get_element(locator).text
class BasePage(object):
    def __init__ (self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.timeout = 30