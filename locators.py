from selenium.webdriver.common.by import By


class LocatorsLogIn:
    SIGN_IN_BUTTON = (By.CLASS_NAME, 'MuiButton-label')
    EMAIL_TEXT_FIELD = (By.NAME, 'email')
    PASSWORD_TEXT_FIELD = (By.NAME, 'password')
    USERNAME_LABEL = (By.XPATH, "//div[@class = 'd-flex flex-column align-items-center']/h4")


class LocatorsHomePage:
    SETTINGS_BUTTON = (By.XPATH, "//div/a[@href='/profile']/button")


class LocatorsSettings:
    CHANGE_USERNAME = (By.ID, ("panel1bh-header"))
    CHANGE_USERNAME_INPUT = (By.NAME, "UserName")
    SUCCESS_NOTIFY = (By.ID, "client-snackbar")
    VERIFY_USERNAME_CHANGE = "Username is changed"
