from tests.conftest import allure_auto_step
from utilities.config_reader import ReadConfig
from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage


@allure_auto_step
class MessagePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __message_tab_button_element = \
        (By.XPATH, "//span[@class and contains(text(), 'Messages')]")
    __notification_not_now_button_element = \
        (By.XPATH, "//button[@class='_a9-- _a9_1']")
    __send_message_button_element = \
        (By.XPATH, "//div[@class and contains(text(), 'Send message')]")
    __recipient_input_element = (By.XPATH, "//input[@placeholder='Search...']")
    __select_recipient_element = \
        (By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 "
                   "x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j "
                   "xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1']")
    __chat_button_element = (By.XPATH, "//div[@role='button' and text()='Chat']")
    __message_input_element = (By.XPATH, "//div[@aria-label='Message']")
    __send_button_element = (By.XPATH, "//div[@role='button' and text()='Send']")
    __sent_message_element = \
        (By.XPATH, f"//span[text()='You: {ReadConfig.get_message_body()}']")
    __sent_time_element = (By.XPATH, "//div[@class='xuxw1ft' and text()='1m']")
    __requests_button_element = (By.XPATH, "//span[@class and text()='Requests']")
    __message_requests_element = (By.XPATH, "//span[@class and text()='Message requests']")
    __hidden_requests_button_element = (By.XPATH, "//span[@class and text()='Hidden Requests']")
    __hidden_requests_element = (By.XPATH, "//span[@class and text()='Hidden requests']")

    def click_message_tab_button(self):
        self.click(self.__message_tab_button_element)
        return self

    def click_notification_not_now_button(self):
        self.click(self.__notification_not_now_button_element)
        return self

    def click_send_message_button(self):
        self.click(self.__send_message_button_element)
        return self

    def set_recipient_name(self, name):
        self.send_keys(self.__recipient_input_element, name)
        return self

    def select_recipient(self):
        self.click(self.__select_recipient_element)
        return self

    def click_chat_button(self):
        self.click(self.__chat_button_element)
        return self

    def write_message(self, message):
        self.send_keys(self.__message_input_element, message)
        return self

    def click_send_button(self):
        self.click(self.__send_button_element)
        return self

    def sent_message_is_displayed(self):
        return self.is_displayed(self.__sent_message_element)

    def sent_time_is_displayed(self):
        return self.is_displayed(self.__sent_time_element)

    def click_requests_button(self):
        self.click(self.__requests_button_element)
        return self

    def message_requests_is_displayed(self):
        return self.is_displayed(self.__message_requests_element)

    def click_hidden_requests_button(self):
        self.click(self.__hidden_requests_button_element)
        return self

    def hidden_requests_is_displayed(self):
        return self.is_displayed(self.__hidden_requests_element)
