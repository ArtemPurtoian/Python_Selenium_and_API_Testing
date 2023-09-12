import pytest
from utilities.config_reader import ReadConfig
from page_objects.login_page import LoginPage
from page_objects.search_panel import SearchPanel


@pytest.mark.regression
def test_search_user(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    search_user = \
        (LoginPage(driver).set_email(email).set_password(password).
         click_login_button().click_search_button().
         input_page_name_to_search(ReadConfig.get_page_name_to_search()).
         click_desired_page().desired_page_is_displayed())
    assert search_user


@pytest.mark.regression
def test_follow_unfollow(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button())
    follow_page_flow = \
        (SearchPanel(driver).click_search_button().
         input_page_name_to_search(ReadConfig.get_page_name_to_search()).
         click_desired_page().click_follow_button().click_following_button().
         click_unfollow_button().follow_button_is_displayed())
    assert follow_page_flow


@pytest.mark.regression
def test_clear_all_history(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    page_name = ReadConfig.get_page_name_to_search()
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button().click_search_button().
     input_page_name_to_search(page_name).click_desired_page().
     click_small_home_button().click_notification_not_now_button().
     click_search_button().click_clear_all_panel_button().
     click_clear_all_confirm_button())
    recently_searched = (SearchPanel(driver).
                         recently_searched_element_is_not_displayed())
    assert recently_searched, "Page is not clear."
