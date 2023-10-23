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
    carenergy = By.XPATH, "//*[contains(@text,'我的岚图')]"
    carexperience = By.XPATH, "//*[contains(@text,'车辆')]"
    intelligent_drive = By.XPATH, "//*[contains(@text,'灯光')]"
    carbody = By.XPATH, "//*[contains(@text,'驾驶偏好')]"
    carsettings = By.XPATH, "//*[contains(@text,'显示')]"
    carabout = By.XPATH, "//*[contains(@text,'声音')]"
    
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
    def click_carenergy(self):
        log.info("正在点击我的岚图按钮")
        self.click(self.carenergy)
        time.sleep(5)
        self.screen('点击我的岚图')
    # Tab栏-点击车辆
    def click_carexperience(self):
        log.info("正在点击车辆按钮")
        self.click(self.carexperience)
        time.sleep(5)
        self.screen('点击车辆')
    # Tab栏-点击灯光
    def click_intelligent_drive(self):
        log.info("正在点击灯光按钮")
        self.click(self.intelligent_drive)
        time.sleep(5)
        self.screen('点击灯光')
    # Tab栏-点击驾驶偏好
    def click_carbody(self):
        log.info("正在点击驾驶偏好")
        self.click(self.carbody)
        time.sleep(5)
        self.screen('点击驾驶偏好')
    # Tab栏-点击显示
    def click_carsettings(self):
        log.info("正在点击显示按钮")
        self.click(self.carsettings)
        time.sleep(5)
        self.screen('点击显示')
    # Tab栏-点击声音
    def click_carabout(self):
        log.info("正在点击声音按钮")
        self.click(self.carabout)
        time.sleep(5)
        self.screen('点击声音')
