from utilities.allure_decorator import allure_auto_step
from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage
from page_objects.home_page import HomePage


@allure_auto_step
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __email_input_element = (By.XPATH, "//input[@name='username']")
    __password_input_element = (By.XPATH, "//input[@name='password']")
    __login_button_element = (By.XPATH, "//button[@type='submit']")
    __google_play_button_element = (By.XPATH,
                                    "//img[@alt='Get it on Google Play']")
    __about_page_button = (By.XPATH, "//span[contains(text(), 'About')]")
    __language_accordion_element = \
        (By.XPATH, "//span[@class='x1ypdohk x1rg5ohu x1n2onr6 x16dsc37']")
    __spanish_language_element = (By.XPATH, "//option[@value='es']")
    __japanese_language_element = (By.XPATH, "//option[@value='ja']")

    def set_email(self, email):
        self.send_keys(self.__email_input_element, email)
        return self

    def set_password(self, password):
        self.send_keys(self.__password_input_element, password)
        return self

    def click_login_button(self):
        self.click(self.__login_button_element)
        return HomePage(self._driver)

    def click_google_play_button(self):
        self.click(self.__google_play_button_element)
        return self

    def click_about_button(self):
        self.click(self.__about_page_button)
        return self

    def click_language_accordion(self):
        self.click(self.__language_accordion_element)
        return self

    def select_spanish_language(self):
        self.click(self.__spanish_language_element)
        return self

    def select_japanese_language(self):
        self.click(self.__japanese_language_element)
        return self

    def is_displayed_language(self):
        return self.is_displayed(self.__japanese_language_element)
