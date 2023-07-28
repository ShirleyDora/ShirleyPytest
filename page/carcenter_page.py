import time
import allure
from base.get_logger import GetLogger
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
# 获取日志入口
log = GetLogger().get_logger()

class CarcenterPage(BaseAction):
    carcenter = By.XPATH, "//*[contains(@text,'车辆')]"
    carenergy = By.XPATH, "//*[contains(@text,'能源管理')]"
    carexperience = By.XPATH, "//*[contains(@text,'驾驶体验')]"
    intelligent_drive = By.XPATH, "//*[contains(@text,'智能驾驶')]"
    carbody = By.XPATH, "//*[contains(@text,'车身设置')]"
    carsettings = By.XPATH, "//*[contains(@text,'通用设置')]"
    carabout = By.XPATH, "//*[contains(@text,'关于本车')]"
    
    @allure.step(title="appcenter页 - 向右滑动屏幕")
    def swipe_to_right(self):
        self.scroll_page_one_time("left")
        self.screen('滑动屏幕')
    # 点击 个人中心图标或文字
    @allure.step(title="车辆页 - 点击 车辆")
    def click_carcenter(self):
        log.info("正在点击车辆按钮")
        self.click(self.carcenter)
        self.screen('点击车辆')
    # 获取 车辆详情页面状态
    @allure.step(title="关于 - 获取 车辆详情页面状态")
    def get_carcenter_txt(self):
        log.info("正在获取车辆详情页面状态")
        self.screen('查看车辆详情页')
        return self.get_feature_text(self.carenergy)
    # 左侧Tab栏
    # Tab栏-点击能量管理
    def click_carenergy(self):
        log.info("正在点击能量管理按钮")
        self.click(self.carenergy)
        time.sleep(5)
        self.screen('点击能量管理')
    # Tab栏-点击驾驶体验
    def click_carexperience(self):
        log.info("正在点击驾驶体验按钮")
        self.click(self.carexperience)
        time.sleep(5)
        self.screen('点击驾驶体验')
    # Tab栏-点击智能驾驶
    def click_intelligent_drive(self):
        log.info("正在点击智能驾驶按钮")
        self.click(self.intelligent_drive)
        time.sleep(5)
        self.screen('点击智能驾驶')
    # Tab栏-点击车身设置
    def click_carbody(self):
        log.info("正在点击车身设置按钮")
        self.click(self.carbody)
        time.sleep(5)
        self.screen('点击车身设置')
    # Tab栏-点击通用设置
    def click_carsettings(self):
        log.info("正在点击通用设置按钮")
        self.click(self.carsettings)
        time.sleep(5)
        self.screen('点击通用设置')
    # Tab栏-点击关于本车
    def click_carabout(self):
        log.info("正在点击关于本车按钮")
        self.click(self.carabout)
        time.sleep(5)
        self.screen('点击关于本车')
