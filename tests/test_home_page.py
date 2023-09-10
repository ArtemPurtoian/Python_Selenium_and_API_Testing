import pytest
from utilities.config_reader import ReadConfig
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage


@pytest.mark.smoke
def test_suggested_pages_count(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    suggested_pages_url = ReadConfig.get_suggested_pages_url()
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button().click_save_info_not_now_button().
     click_notification_not_now_button().click_see_all_button().
     wait_url_to_be(suggested_pages_url))
    last_suggested_page = HomePage(driver).last_suggested_page_is_displayed()
    assert last_suggested_page


@pytest.mark.smoke
def test_switch_to_profile_from_home_page(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button().click_save_info_not_now_button().
     click_notification_not_now_button().click_user_label_panel_button().
     click_home_button().click_user_label_header_button())
    user_profile_url = ReadConfig.get_user_profile_url()
    assert user_profile_url == driver.current_url


@pytest.mark.smoke
def test_loading_spinner_is_displayed(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button().click_save_info_not_now_button().
     click_notification_not_now_button().continuously_scroll_to_bottom())
    loading_spinner = HomePage(driver).loading_spinner_is_displayed()
    assert loading_spinner


@pytest.mark.smoke
def test_switch_appearance(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button().click_more_button().click_switch_appearance_button())
    if HomePage(driver).dark_mode_is_displayed():
        HomePage(driver).click_dark_mode_button()
        assert HomePage(driver).light_mode_is_displayed(), \
            "Dark mode is displayed."
    elif HomePage(driver).light_mode_is_displayed():
        HomePage(driver).click_dark_mode_button()
        assert HomePage(driver).dark_mode_is_displayed(), \
            "Light mode is displayed."


@pytest.mark.smoke
def test_search_panel_is_displayed(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button().click_search_button())
    assert HomePage(driver).search_panel_is_displayed()
