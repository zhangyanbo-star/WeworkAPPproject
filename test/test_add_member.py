from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAddMember:
    def setup(self):
        desired_caps = dict()
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "127.0.0.1:7555"
        desired_caps["appPackage"] = "com.tencent.wework"
        desired_caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 默认false，会把登录信息全部清空，设置成true，不清空本地缓存，启动APP
        desired_caps["noReset"] = "true"
        # 设置页面等待空闲状态的时间-渲染当前页面的时间-0秒，工作中一般1秒2秒就够用了
        desired_caps["settings[waitForIdleTimeout]"] = 2

        # 和server建立连接，告诉server设备信息
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_add_member(self):
        name = "Kaido"
        gender = "男"
        phone = "10000001113"
        mailbox = "Kaido@163.com"
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('
                                                               'new UiSelector().scrollable(true).instance(0))'
                                                               '.scrollIntoView('
                                                               'new UiSelector().text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/..//*[@text="必填"]').send_keys("Cyobba")
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/..//*[@text="必填"]').send_keys(name)
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"性别")]/..//*[@text="男"]').click()
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        elif gender == "女":
            self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys(phone)
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"邮箱")]/..//*[@text="选填"]').send_keys(mailbox)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        result = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert result == "添加成功"
