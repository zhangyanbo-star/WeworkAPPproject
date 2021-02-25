from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        return self.find(locator).click()

    def find_and_sendkeys(self, locator, text):
        return self.find(locator).send_keys(text)

    def scoll_find_click(self, text):
        # text("{text}")，写成text({text})会报错
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
                                                                      'new UiSelector().scrollable(true).instance(0))'
                                                                      '.scrollIntoView('
                                                                      f'new UiSelector().text("{text}").instance(0));').click()
