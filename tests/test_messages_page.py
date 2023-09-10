import pytest
from utilities.config_reader import ReadConfig
from page_objects.login_page import LoginPage
from page_objects.messages_page import MessagePage


@pytest.mark.regression
def test_send_message(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button())
    (MessagePage(driver).click_message_tab_button().
     click_notification_not_now_button().click_send_message_button().
     set_recipient_name(ReadConfig.get_message_recipient()).select_recipient().
     click_chat_button().write_message(ReadConfig.get_message_body()).
     click_send_button())
    sent_message = MessagePage(driver).sent_message_is_displayed()
    sent_time = MessagePage(driver).sent_time_is_displayed()
    assert sent_message and sent_time == "1m"


@pytest.mark.smoke
def test_requests_page_is_displayed(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button())
    (MessagePage(driver).click_message_tab_button().
     click_notification_not_now_button().click_requests_button())
    message_requests = MessagePage(driver).message_requests_is_displayed()
    assert message_requests


@pytest.mark.smoke
def test_hidden_requests_page_is_displayed(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button())
    (MessagePage(driver).click_message_tab_button().
     click_notification_not_now_button().click_requests_button().
     click_hidden_requests_button())
    hidden_requests = MessagePage(driver).hidden_requests_is_displayed()
    assert hidden_requests
