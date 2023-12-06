import time
import allure
from base.get_logger import GetLogger
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from base.base_analyze import analyze_data
import pytest
# 获取日志入口
log = GetLogger().get_logger()

# @pytest.mark.parametrize("args", analyze_data("carcenter_page_data", "test_carcenter_page"))
# class CarcenterPage(BaseAction,args):
    # # 解析数据
    # xpath = args["xpath"]
    # titleText = args["titleText)"]  
    # stepInfo = args["stepInfo"] 
    # screen = args["screen"] 
    # assertText = args["assertText"] 
    # toast = args["toast"]
    # log.info("当前xpath为:%s,title为:%s,stepInfo为:%s,screen:%s,assertText:%s,toast:%s" % (xpath, title, stepInfo,screen,assertText,toast))
    # # 定义左边ITEM
    # itemText = By.XPATH,xpath
    # # 点击ITEM
    # @allure.step(title=titleText)
    # def click_itemTab(self):
    #     log.info(stepInfo)
    #     self.click(self.itemText)
    #     self.screen(screen)
    
class CarcenterPage(BaseAction):
    carcenter = By.XPATH, "//*[contains(@text,'设置')]"
    my_lantu = By.XPATH, "//*[contains(@text,'我的岚图')]"
    vehicle = By.XPATH, "//*[contains(@text,'车辆')]"
    lighting = By.XPATH, "//*[contains(@text,'灯光')]"
    driving_preferences = By.XPATH, "//*[contains(@text,'驾驶偏好')]"
    driving_assistant = By.XPATH, "//*[contains(@text,'驾驶辅助')]"
    display = By.XPATH, "//*[contains(@text,'显示')]"
    sound = By.XPATH, "//*[contains(@text,'声音')]"
    connect = By.XPATH, "//*[contains(@text,'连接')]"
    security = By.XPATH, "//*[contains(@text,'安全维护')]"
    system = By.XPATH, "//*[contains(@text,'系统')]"

    @allure.step(title="appcenter页 - 向右滑动屏幕")
    def swipe_to_right(self):
        self.scroll_page_one_time("left")
        self.screen('滑动屏幕')
    # 点击 个人中心图标或文字
    @allure.step(title="设置页 - 点击设置")
    def click_carcenter(self):
        log.info("正在点击设置按钮")
        self.click(self.carcenter)
        self.screen('点击设置')
    # 获取设置页面状态
    @allure.step(title="关于 - 获取设置页面状态")
    def get_carcenter_txt(self):
        log.info("正在获取设置页面状态")
        self.screen('查看设置页')
        return self.get_feature_text(self.carenergy)
    # 左侧Tab栏
    # Tab栏-点击我的岚图
    def click_my_lantu(self):
        log.info("正在点击我的岚图按钮")
        self.click(self.my_lantu)
        time.sleep(2)
        self.screen('点击我的岚图')
    # Tab栏-点击车辆
    def click_vehicle(self):
        log.info("正在点击车辆按钮")
        self.click(self.vehicle)
        time.sleep(2)
        self.screen('点击车辆')
    # Tab栏-点击灯光
    def click_lighting(self):
        log.info("正在点击灯光按钮")
        self.click(self.lighting)
        time.sleep(2)
        self.screen('点击灯光')
    # Tab栏-点击驾驶偏好
    def click_driving_preferences(self):
        log.info("正在点击驾驶偏好")
        self.click(self.driving_preferences)
        time.sleep(2)
        self.screen('点击驾驶偏好')
    # Tab栏-点击驾驶辅助
    def click_driving_assistant(self):
        log.info("正在点击驾驶辅助")
        self.click(self.driving_assistant)
        time.sleep(2)
        self.screen('点击驾驶辅助')
    # Tab栏-点击显示
    def click_display(self):
        log.info("正在点击显示按钮")
        self.click(self.display)
        time.sleep(2)
        self.screen('点击显示')
    # Tab栏-点击声音
    def click_sound(self):
        log.info("正在点击声音按钮")
        self.click(self.sound)
        time.sleep(2)
        self.screen('点击声音')
    # Tab栏-点击连接
    def click_connect(self):
        log.info("正在点击连接按钮")
        self.click(self.connect)
        time.sleep(2)
        self.screen('点击连接')
    # Tab栏-点击安全维护
    def click_security(self):
        log.info("正在点击安全维护按钮")
        self.click(self.security)
        time.sleep(2)
        self.screen("点击安全维护")
    # Tab栏-点击系统
    def click_system(self):
        log.info("正在点击系统按钮")
        self.click(self.system)
        time.sleep(2)
        self.screen("点击系统")


