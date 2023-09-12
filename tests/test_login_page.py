import pytest
import datetime
from utilities.config_reader import ReadConfig
from utilities.web_ui.base_page import BasePage
from page_objects.login_page import LoginPage


@pytest.mark.smoke
def test_page_title(initialize_driver):
    driver = initialize_driver
    actual_title = ReadConfig.get_app_title()
    assert actual_title == driver.title, \
        f"The title is not '{ReadConfig.get_app_title()}'"


@pytest.mark.regression
def test_login_logout(open_login_page):
    base_url = ReadConfig.get_app_base_url()
    current_url = (open_login_page.click_more_button().click_logout_button().
                   wait_url_to_be(base_url).get_current_url())
    assert base_url == current_url, "Invalid URL."


@pytest.mark.smoke
def test_google_play_link(initialize_driver):
    driver = initialize_driver
    LoginPage(driver).click_google_play_button().wait_windows_number_to_be_2()
    google_play_app_url = driver.current_url
    BasePage(driver).wait_url_to_be(google_play_app_url)
    assert google_play_app_url == driver.current_url, "Invalid URL."


@pytest.mark.smoke
def test_about_window_opened(initialize_driver):
    driver = initialize_driver
    about_tab_url = ReadConfig.get_about_tab_url()
    (LoginPage(driver).click_about_button().wait_windows_number_to_be_2().
     wait_url_to_be(about_tab_url))
    assert about_tab_url == driver.current_url, "Invalid URL."


@pytest.mark.regression
def test_change_language(initialize_driver):
    driver = initialize_driver
    final_language = (LoginPage(driver).click_language_accordion().
                      select_spanish_language().click_language_accordion().
                      select_japanese_language())
    assert final_language.is_displayed_language(), "Language wasn't changed."


@pytest.mark.regression
def test_footer_current_year(initialize_driver):
    footer_date_string = ReadConfig.get_footer_date_string()
    today = datetime.date.today()
    year = today.year
    assert str(year) in footer_date_string, "Incorrect year."
