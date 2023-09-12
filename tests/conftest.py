import pytest
from utilities.driver_factory import create_drivers
from utilities.config_reader import ReadConfig
from contextlib import suppress
import allure
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.messages_page import MessagePage


@pytest.fixture
def initialize_driver(request):
    driver = create_drivers(ReadConfig.get_browser_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_app_base_url())
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def open_login_page(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button())
    return HomePage(driver)


@pytest.fixture
def open_messages_page(initialize_driver):
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    driver = initialize_driver
    (LoginPage(driver).set_email(email).set_password(password).
     click_login_button())
    (MessagePage(driver).click_message_tab_button().
     click_notification_not_now_button())
    return MessagePage(driver)


@pytest.fixture
def search_user(open_login_page):
    searched_user = \
        (open_login_page.click_search_button().
         input_page_name_to_search(ReadConfig.get_page_name_to_search()).
         click_desired_page())
    return searched_user


@pytest.fixture
def open_user_page(open_login_page):
    user_page = open_login_page.open_user_profile()
    return user_page
