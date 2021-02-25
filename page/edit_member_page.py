from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


class EditMemberPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    def edit_name(self, name):
        # self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/..//*[@text="必填"]').send_keys(name)
        self.find_and_sendkeys((MobileBy.XPATH, '//*[contains(@text,"姓名")]/..//*[@text="必填"]'), name)
        return self

    def edit_gender(self, gender):
        # self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"性别")]/..//*[@text="男"]').click()
        self.find_and_click((MobileBy.XPATH, '//*[contains(@text,"性别")]/..//*[@text="男"]'))

        # 如果弹窗弹出的速度比代码运行的速度慢时，会报错-元素不在DOM树中，加处理-显示等待
        locator_nan = (MobileBy.XPATH, '//*[@text="男"]')
        locator_nv = (MobileBy.XPATH, '//*[@text="女"]')

        if gender == "男":
            # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator_nan)).click()
        elif gender == "女":
            # self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator_nv)).click()
        return self

    def edit_phone(self, phone):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys(phone)
        self.find_and_sendkeys((MobileBy.XPATH, '//*[@text="手机号"]'), phone)
        return self

    def edit_mailbox(self, mailbox):
        # self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"邮箱")]/..//*[@text="选填"]').send_keys(mailbox)
        self.find_and_sendkeys((MobileBy.XPATH, '//*[contains(@text,"邮箱")]/..//*[@text="选填"]'), mailbox)
        return self

    def click_save(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        self.find_and_click((MobileBy.XPATH, '//*[@text="保存"]'))
        from page.add_manually_page import AddManuallyPage
        return AddManuallyPage(self.driver)
