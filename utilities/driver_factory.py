from selenium import webdriver


CHROME = 1
EDGE = 2
FIREFOX = 3


def create_drivers(driver_id):
    if int(driver_id) == CHROME:
        driver = webdriver.Chrome()
        return driver
    elif int(driver_id) == EDGE:
        driver = webdriver.Edge()
        return driver
    elif int(driver_id) == FIREFOX:
        driver = webdriver.Firefox()
        return driver
    else:
        driver = webdriver.Chrome()
        return driver
