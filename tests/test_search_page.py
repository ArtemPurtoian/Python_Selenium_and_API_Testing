import pytest


@pytest.mark.regression
def test_search_user(search_user):
    searched_user = search_user.is_displayed_desired_page()
    assert searched_user, "The user is not displayed."


@pytest.mark.regression
def test_follow_unfollow(search_user):
    follow_page_flow = \
        (search_user.click_follow_button().click_following_button().
         click_unfollow_button().is_displayed_follow_button())
    assert follow_page_flow, "The user hasn't been unfollowed."


@pytest.mark.regression
def test_clear_all_history(search_user):
    recently_searched = \
        (search_user.click_small_home_button().
         click_notification_not_now_button().click_search_button().
         click_clear_all_panel_button().click_clear_all_confirm_button().
         is_not_displayed_recently_searched_element())
    assert recently_searched, "History is not clear."
