from appium import webdriver


def init_driver(no_reset=True):
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['appPackage'] = 'me.ele'
    desired_caps['appActivity'] = 'com.ali.user.mobile.login.ui.UserLoginActivity'
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['noReset'] = no_reset

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# ba8749b7或M2012K11AC

if __name__ == '__main__':
    init_driver()
