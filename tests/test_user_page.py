import pytest
from utilities.config_reader import ReadConfig


@pytest.mark.regression
def test_collection_e2e(open_user_page):
    collection_created = \
        (open_user_page.click_saved_page_button().click_new_collection().
         set_new_collection_name(ReadConfig.get_new_collection_name()).
         click_next_button().click_done_button().is_displayed_start_saving())
    assert collection_created, "Collection hasn't been created."
    collection_edited = \
        (collection_created.click_edit_settings_button().
         click_edit_collection_button().
         edit_collection_name(ReadConfig.get_edited_collection_name()).
         click_done_button().is_displayed_start_saving())
    assert collection_edited, "Collection hasn't been edited."
    image_added = (collection_edited.click_edit_settings_button().
                   click_add_from_saved_button().add_element_from_saved().
                   click_done_button().is_displayed_image())
    assert image_added, "Image hasn't been added."
    collection_deleted = (image_added.click_edit_settings_button().
                          delete_collection().is_not_displayed_collection())
    assert collection_deleted, "Collection hasn't been deleted."


@pytest.mark.regression
def test_edit_profile(open_user_page):
    profile_edited = \
        (open_user_page.click_edit_profile_button().
         edit_bio(ReadConfig.get_bio_info()).click_gender_button().
         select_male_gender().click_done_button().click_submit_button().
         is_displayed_profile_saved_popup())
    assert profile_edited, "Profile hasn't been edited."
