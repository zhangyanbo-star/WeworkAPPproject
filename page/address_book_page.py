from appium.webdriver.common.mobileby import MobileBy

from page.add_manually_page import AddManuallyPage
from page.base_page import BasePage


class AddressBookPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_add_member(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
        #                                                        'new UiSelector().scrollable(true).instance(0))'
        #                                                        '.scrollIntoView('
        #                                                        'new UiSelector().text("添加成员").instance(0));').click()
        self.scoll_find_click("添加成员")
        return AddManuallyPage(self.driver)
