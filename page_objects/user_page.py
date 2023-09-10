from tests.conftest import allure_auto_step
from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage


@allure_auto_step
class UserPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __user_label_element = (By.XPATH, "//span[contains(text(), 'Profile')]")
    __saved_page_button_element = (By.XPATH, "//span[contains(text(), 'Saved')]")
    __new_collection_button_element = (By.XPATH, "//div[contains(text(), 'New Collection')]")
    __collection_name_input_element = (By.XPATH, "//input[@name='collectionName']")
    __next_button_element = (By.XPATH, "//button[contains(text(), 'Next')]")
    __done_button_element = (By.XPATH, "//button[contains(text(), 'Done')]")
    __start_saving_element = (By.XPATH, "//span[contains(text(), 'Start Saving')]")
    __edit_settings_button_element = (By.CSS_SELECTOR, "svg[aria-label='Edit options']")
    __edit_collection_button_element = (By.XPATH, "//button[contains(text(), 'Edit collection')]")
    __add_from_saved_button_element = (By.XPATH, "//button[contains(text(), 'Add from saved')]")
    __add_element_from_saved = (By.XPATH, "(//div[@class])[149]")
    __image_displayed_element = (By.XPATH, "//div[@class='_aagu']")
    __delete_collection_button = (By.XPATH, "//button[contains(text(), 'Delete collection')]")
    __confirm_delete_coll_button = (By.XPATH, "//button[contains(text(), 'Delete')]")
    __deleted_collection_element = (By.XPATH, "//span[@class and text()='Edited collection 1']")
    __edit_profile_button_element = (By.XPATH, "//a[@class and text()='Edit profile']")
    __bio_input_element = (By.XPATH, "//textarea")
    __gender_selection_element = (By.XPATH, "//input[@id='pepGender']")
    __male_gender_element = (By.XPATH, "//input[@value='1']")
    __submit_button_element = (By.XPATH, "//div[@role='button' and text()='Submit']")
    __profile_saved_popup_element = (By.XPATH, "//p[@class='_abmp']")

    def click_user_label(self):
        self.click(self.__user_label_element)
        return self

    def click_saved_page_button(self):
        self.click(self.__saved_page_button_element)
        return self

    def click_new_collection(self):
        self.click(self.__new_collection_button_element)
        return self

    def set_new_collection_name(self, collection_name):
        self.send_keys(self.__collection_name_input_element, collection_name)
        return self

    def click_next_button(self):
        self.click(self.__next_button_element)
        return self

    def click_done_button(self):
        self.click(self.__done_button_element)
        return self

    def start_saving_is_displayed(self):
        return self.is_displayed(self.__start_saving_element)

    def click_edit_settings_button(self):
        self.click(self.__edit_settings_button_element)
        return self

    def click_edit_collection_button(self):
        self.click(self.__edit_collection_button_element)
        return self

    def edit_collection_name(self, new_name):
        self.clear_element_via_js(self._driver,
                                  self.__collection_name_input_element)
        self.send_keys(self.__collection_name_input_element, new_name)
        return self

    def click_add_from_saved_button(self):
        self.click(self.__add_from_saved_button_element)
        return self

    def add_element_from_saved(self):
        self.click(self.__add_element_from_saved)
        return self

    def image_is_displayed(self):
        return self.is_displayed(self.__image_displayed_element)

    def delete_collection(self):
        self.click(self.__delete_collection_button)
        self.click(self.__confirm_delete_coll_button)
        return self

    def collection_is_deleted(self):
        return self.is_not_displayed(self.__deleted_collection_element)

    def click_edit_profile_button(self):
        self.click(self.__edit_profile_button_element)
        return self

    def edit_bio(self, bio_info):
        self.clear_element_via_js(self._driver, self.__bio_input_element)
        self.send_keys(self.__bio_input_element, bio_info)
        return self

    def click_gender_button(self):
        self.click(self.__gender_selection_element)
        return self

    def select_male_gender(self):
        self.click(self.__male_gender_element)
        return self

    def click_submit_button(self):
        self.click(self.__submit_button_element)
        return self

    def profile_saved_popup_is_displayed(self):
        return self.is_displayed(self.__profile_saved_popup_element)
