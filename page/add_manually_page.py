from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.edit_member_page import EditMemberPage


class AddManuallyPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_add_manually(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.find_and_click((MobileBy.XPATH, '//*[@text="手动输入添加"]'))
        return EditMemberPage(self.driver)

    def get_toast(self):
        # result = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        result = self.find((MobileBy.XPATH, '//*[@class="android.widget.Toast"]')).text
        return result
