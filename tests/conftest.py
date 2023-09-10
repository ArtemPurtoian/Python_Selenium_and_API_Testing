import pytest
from utilities.driver_factory import create_drivers
from utilities.config_reader import ReadConfig
from contextlib import suppress
import allure
import inspect


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


def allure_auto_step(cls):
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        if name != "__init__":
            setattr(cls, name, allure.step(method))
    return cls
