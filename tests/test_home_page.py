import pytest
from utilities.config_reader import ReadConfig
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage


@pytest.mark.smoke
def test_suggested_pages_count(open_login_page):
    suggested_pages_url = ReadConfig.get_suggested_pages_url()
    last_suggested_page = \
        (open_login_page.click_save_info_not_now_button().
         click_notification_not_now_button().click_see_all_button().
         wait_url_to_be(suggested_pages_url).is_displayed_last_suggested_page())
    assert last_suggested_page, "The amount of suggested pages in incorrect."


@pytest.mark.smoke
def test_switch_to_profile_from_home_page(open_login_page):
    user_profile_url = ReadConfig.get_user_profile_url()
    current_url = \
        (open_login_page.click_save_info_not_now_button().
         click_notification_not_now_button().click_user_label_panel_button().
         click_home_button().click_user_label_header_button().get_current_url())
    assert user_profile_url == current_url, "Incorrect URL."


@pytest.mark.smoke
def test_loading_spinner_is_displayed(open_login_page):
    loading_spinner = \
        (open_login_page.click_save_info_not_now_button().
         click_notification_not_now_button().continuously_scroll_to_bottom().
         is_displayed_loading_spinner())
    assert loading_spinner, "The loading spinner is not displayed."


@pytest.mark.smoke
def test_switch_appearance(open_login_page):
    appearance = (open_login_page.click_more_button().
                  click_switch_appearance_button())
    if appearance.is_displayed_dark_mode():
        appearance.click_dark_mode_button()
        assert appearance.is_displayed_light_mode(), \
            "Dark mode is displayed."
    elif appearance.is_displayed_light_mode():
        appearance.click_dark_mode_button()
        assert appearance.is_displayed_dark_mode(), \
            "Light mode is displayed."


@pytest.mark.smoke
def test_search_page_is_displayed(open_login_page):
    search_page = \
        (open_login_page.click_search_button().is_displayed_search_page())
    assert search_page, "The search page is not displayed."
