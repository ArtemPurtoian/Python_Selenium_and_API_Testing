from tests.conftest import allure_auto_step
from utilities.config_reader import ReadConfig
from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage
from page_objects.search_panel import SearchPanel


@allure_auto_step
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __more_button_element = (By.XPATH, "//span[contains(text(), 'More')]")
    __logout_button_element = (By.XPATH, "//span[contains(text(),'Log out')]")
    __save_info_not_now_button_element = \
        (By.XPATH, "//div[@role='button' and text()='Not Now']")
    __notification_not_now_button_element = \
        (By.XPATH, "//button[@class='_a9-- _a9_1']")
    __see_all_button_element = \
        (By.XPATH, "//span[@class and text()='See All']")
    __suggested_pages_element = \
        (By.XPATH,
         "//div[@class='x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3']")
    __last_suggested_element = \
        (By.XPATH,
         "//div[@class='x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3']"
                                          "[30]")
    __user_label_panel_element = \
        (By.XPATH, "//span[contains(text(), 'Profile')]")
    __user_label_header_element = \
        (By.XPATH, f"//a[@class and text()='{ReadConfig.get_user_name()}']")
    __home_button_element = (By.XPATH, "//span[@class and text()='Home']")
    __loading_spinner_element = \
        (By.XPATH, "//div[@data-visualcompletion='loading-state']")
    __switch_appearance_button = \
        (By.XPATH, "//span[text()='Switch appearance']")
    __dark_mode_button = (By.XPATH, "//span[text()='Dark mode']")
    __appearance_back_button = \
        (By.XPATH, "(//div[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k'])[2]")
    __dark_mode = (By.XPATH, "//html[@class='_9dls js-focus-visible _aa4d']")
    __light_mode = (By.XPATH, "//html[@class='_9dls js-focus-visible _aa4c']")
    __search_button_element = (By.XPATH, "//span[@class and text()='Search']")
    __search_panel_element = (By.XPATH, "//div[@class='_aaw6']")

    def click_more_button(self):
        self.click(self.__more_button_element)
        return self

    def click_logout_button(self):
        self.click(self.__logout_button_element)
        return self

    def click_notification_not_now_button(self):
        self.click(self.__notification_not_now_button_element)
        return self

    def click_see_all_button(self):
        self.click(self.__see_all_button_element)
        return self

    def click_save_info_not_now_button(self):
        self.click(self.__save_info_not_now_button_element)
        return self

    def last_suggested_page_is_displayed(self):
        return self.is_displayed(self.__last_suggested_element)

    def click_user_label_panel_button(self):
        self.click(self.__user_label_panel_element)
        return self

    def click_user_label_header_button(self):
        self.click(self.__user_label_header_element)
        return self

    def click_home_button(self):
        self.click(self.__home_button_element)
        return self

    def loading_spinner_is_displayed(self):
        return self.is_displayed(self.__loading_spinner_element)

    def click_switch_appearance_button(self):
        self.click(self.__switch_appearance_button)
        return self

    def click_dark_mode_button(self):
        self.click(self.__dark_mode_button)
        return self

    def click_appearance_back_button(self):
        self.click(self.__appearance_back_button)
        return self

    def light_mode_is_displayed(self):
        return self.is_displayed(self.__light_mode)

    def dark_mode_is_displayed(self):
        return self.is_displayed(self.__dark_mode)

    def click_search_button(self):
        self.click(self.__search_button_element)
        return SearchPanel(self._driver)

    def search_panel_is_displayed(self):
        return self.is_displayed(self.__search_panel_element)
