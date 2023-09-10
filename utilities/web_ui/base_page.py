from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 10)

    def __wait_until_element_is_visible(self, locator: tuple):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def __wait_until_element_is_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.__wait_until_element_is_clickable(locator).click()

    def send_keys(self, locator, value):
        element = self.__wait_until_element_is_visible(locator)
        element.send_keys(value)

    def wait_url_to_be(self, url):
        self.__wait.until(EC.url_to_be(url))
        return self

    def wait_windows_number_to_be_2(self):
        self.__wait.until(EC.number_of_windows_to_be(2))
        window_handles = self._driver.window_handles
        self._driver.switch_to.window(window_handles[-1])
        return self

    def wait_title_to_be(self, page_title):
        self.__wait.until(EC.title_contains(page_title))
        return self

    def clear_element_via_js(self, driver, locator):
        element = self.__wait_until_element_is_visible(locator)
        driver.execute_script("arguments[0].value = '';", element)
        return self

    def continuously_scroll_to_bottom(self):
        scroll_count = 0
        while scroll_count < 6:
            (self._driver.execute_script
             ("window.scrollTo(0, document.body.scrollHeight);"))
            scroll_count += 1
        return self

    def is_displayed(self, locator):
        return (self.__wait.until(EC.visibility_of_element_located(locator)).
                is_displayed())

    def is_not_displayed(self, locator):
        return self.__wait.until(EC.invisibility_of_element_located(locator))
