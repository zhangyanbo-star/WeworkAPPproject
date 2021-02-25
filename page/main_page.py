from appium.webdriver.common.mobileby import MobileBy

from page.address_book_page import AddressBookPage
from page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_address_book(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 传入一个元祖
        self.find_and_click((MobileBy.XPATH, '//*[@text="通讯录"]'))
        return AddressBookPage(self.driver)
