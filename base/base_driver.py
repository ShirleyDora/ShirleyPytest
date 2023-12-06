# 安装pip install appium-python-client==2.11.0,
# appium2.0代码安装npm install appium@next
from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
from base.base_analyze import settings_read_yaml
# from appium.options.common import AppiumOptions
def init_driver(no_reset=True):
    caps = {}
    caps["platformName"] = "Android"
    caps["appium:automationName"] = "UiAutomator2"
    # caps["appium:deviceName"] = "e84cdc46"
    caps["appium:deviceName"] = settings_read_yaml("config","devicename")
    caps["appium:ensureWebviewsHavePages"] = True
    caps["appium:nativeWebScreenshot"] = True
    caps["appium:newCommandTimeout"] = 3600
    caps["appium:connectHardwareKeyboard"] = True
    caps["appium:noReset"] = no_reset
    caps["appium:skipServerInstallation"]= False
    url="http://127.0.0.1:4723"
    driver = webdriver.Remote(url, caps)
    # option = AppiumOptions()
    # option.set_capability("platformName","Android")
    # option.set_capability("appium:automationName","UiAutomator2")
    # url="http://127.0.0.1:4723"
    # driver = webdriver.Remote(url,options=option)
    return driver
    
    # desired_caps = dict()
    # desired_caps['platformVersion'] = '11.0'
    # desired_caps['appPackage'] = 'com.voyah.os.carlauncher'
    # desired_caps['appActivity'] = 'com.voyah.os.carlauncher.second.LauncherActivityMainSecond'

if __name__ == '__main__':
    init_driver()
