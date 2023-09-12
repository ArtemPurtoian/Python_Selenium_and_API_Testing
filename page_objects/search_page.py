from tests.conftest import allure_auto_step
from utilities.config_reader import ReadConfig
from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage


@allure_auto_step
class SearchPanel(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __search_button_element = (By.XPATH, "//span[@class and text()='Search']")
    __search_button_small_element = \
        (By.XPATH, "//div[@class='x9f619 xxk0z11 xii2z7h x11xpdln x19c4wfv xvy4d1p']")
    __search_input_element = (By.XPATH, "//input[@aria-label='Search input']")
    __desired_page_search_element = \
        (By.XPATH, f"//span[@class and text()='{ReadConfig.get_page_name_to_search()}']")
    __desired_page_title_element = \
        (By.XPATH, f"//h2[text()='{ReadConfig.get_page_name_to_search()}']")
    __follow_button_element = (
        By.XPATH, "//div[@class='_aacl _aaco _aacw _aad6 _aade' and text()='Follow']")
    __following_button_element = \
        (By.XPATH, "//div[@class='_aacl _aaco _aacw _aad6 _aade' and text()='Following']")
    __unfollow_button_element = \
        (By.XPATH, "//span[@class and text()='Unfollow']")
    __small_home_button_element = \
        (By.XPATH, "//div[@class='_aagx']")
    __notification_not_now_button_element = \
        (By.XPATH, "//button[@class='_a9-- _a9_1']")
    __clear_all_panel_element = \
        (By.XPATH, "//div[@class and text()='Clear all']")
    __clear_all_confirm_element = \
        (By.XPATH, "//button[@class='_a9-- _a9-_' and text()='Clear all']")
    __recently_searched_element = \
        (By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 "
                   "x5pf9jr xo71vjh xxbr6pl xbbxn1n xwib8y2 x1y1aw1k x1uhb9sk "
                   "x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 "
                   "x1oa3qoh x1nhvcw1']")

    def click_search_button(self):
        self.click(self.__search_button_element)
        return self

    def click_small_search_button(self):
        self.click(self.__search_button_small_element)
        return self

    def input_page_name_to_search(self, page_name):
        self.send_keys(self.__search_input_element, page_name)
        return self

    def click_desired_page(self):
        self.click(self.__desired_page_search_element)
        return self

    def click_follow_button(self):
        self.click(self.__follow_button_element)
        return self

    def click_following_button(self):
        self.click(self.__following_button_element)
        return self

    def click_unfollow_button(self):
        self.click(self.__unfollow_button_element)
        return self

    def follow_button_is_displayed(self):
        return self.is_displayed(self.__follow_button_element)

    def desired_page_is_displayed(self):
        return self.is_displayed(self.__desired_page_title_element)

    def click_small_home_button(self):
        self.click(self.__small_home_button_element)
        return self

    def click_notification_not_now_button(self):
        self.click(self.__notification_not_now_button_element)
        return self

    def click_clear_all_panel_button(self):
        self.click(self.__clear_all_panel_element)
        return self

    def click_clear_all_confirm_button(self):
        self.click(self.__clear_all_confirm_element)
        return self

    def recently_searched_element_is_not_displayed(self):
        return self.is_not_displayed(self.__recently_searched_element)
