import pytest
from utilities.config_reader import ReadConfig


@pytest.mark.regression
def test_send_message(open_messages_page):
    (open_messages_page.click_send_message_button().
     set_recipient_name(ReadConfig.get_message_recipient()).
     select_recipient().click_chat_button().
     write_message(ReadConfig.get_message_body()).click_send_button())
    sent_message = open_messages_page.is_displayed_sent_message()
    sent_time = open_messages_page.is_displayed_sent_time()
    assert sent_message, "Message hasn't been sent."
    assert sent_time, "Sent time is incorrect."


@pytest.mark.smoke
def test_requests_page_is_displayed(open_messages_page):
    message_requests = (open_messages_page.click_requests_button().
                        is_displayed_message_requests())
    assert message_requests, "Requests page is not displayed."


@pytest.mark.smoke
def test_hidden_requests_page_is_displayed(open_messages_page):
    hidden_requests = \
        (open_messages_page.click_requests_button().
         click_hidden_requests_button().is_displayed_hidden_requests())
    assert hidden_requests, "Hidden requests page is not displayed."
