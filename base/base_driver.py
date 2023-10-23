# 安装pip install appium-python-client==2.11.0,
# appium2.0代码安装npm install appium@next
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from base.base_analyze import settings_read_yaml
def init_driver(no_reset=True):
    caps = {}
    caps["platformName"] = "Android"
    caps["appium:automationName"] = "UiAutomator2"
    caps["appium:deviceName"] = "697ea58c"
    caps["appium:ensureWebviewsHavePages"] = True
    caps["appium:nativeWebScreenshot"] = True
    caps["appium:newCommandTimeout"] = 3600
    caps["appium:connectHardwareKeyboard"] = True
    caps["appium:noReset"] = no_reset
    driver = webdriver.Remote("http://127.0.0.1:4723", caps)
    return driver
    
    # desired_caps = dict()
    # desired_caps['platformVersion'] = '11.0'
    # desired_caps['appPackage'] = 'com.voyah.os.carlauncher'
    # desired_caps['appActivity'] = 'com.voyah.os.carlauncher.second.LauncherActivityMainSecond'

if __name__ == '__main__':
    init_driver()
