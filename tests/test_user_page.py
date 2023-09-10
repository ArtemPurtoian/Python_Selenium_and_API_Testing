import pytest
from utilities.config_reader import ReadConfig
from page_objects.login_page import LoginPage
from page_objects.user_page import UserPage


@pytest.mark.regression
def test_collection_e2e(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button())
    collection_created = (
        UserPage(driver).click_user_label().click_saved_page_button().
        click_new_collection().
        set_new_collection_name(ReadConfig.get_new_collection_name()).
        click_next_button().click_done_button().start_saving_is_displayed())
    assert collection_created
    collection_edited = (
        UserPage(driver).click_edit_settings_button().
        click_edit_collection_button().
        edit_collection_name(ReadConfig.get_edited_collection_name()).
        click_done_button().start_saving_is_displayed())
    assert collection_edited
    image_added = (UserPage(driver).click_edit_settings_button().
                   click_add_from_saved_button().add_element_from_saved().
                   click_done_button().image_is_displayed())
    assert image_added
    collection_deleted = (UserPage(driver).click_edit_settings_button().
                          delete_collection().collection_is_deleted())
    assert collection_deleted


@pytest.mark.regression
def test_edit_profile(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button())
    profile_edited = (
        UserPage(driver).click_user_label().click_edit_profile_button().
        edit_bio(ReadConfig.get_bio_info()).click_gender_button().
        select_male_gender().click_done_button().click_submit_button().
        profile_saved_popup_is_displayed())
    assert profile_edited
