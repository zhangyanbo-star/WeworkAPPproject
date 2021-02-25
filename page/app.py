from appium import webdriver

from page.base_page import BasePage
from page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
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
        else:
            # 拿到appPackage和appActivity启动APP
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        # 先退出再启动
        self.driver.quit()
        self.driver.launch_app()

    def goto_main(self):
        return MainPage(self.driver)
