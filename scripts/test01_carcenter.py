import time
import os,sys
sys.path.append(os.getcwd())
import allure
from base.get_logger import GetLogger
from base.base_driver import init_driver
from page.page import Page
from base.base_action import BaseAction
import pytest
import allure
# 获取日志入口
log = GetLogger().get_logger()

class TestCarcenter:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.base = BaseAction(self.driver)
        # 等待广告
        time.sleep(5)
        # self.initlog = BaseAction(self.initlog())
        

    def teardown(self):
        self.driver.quit()
        # self.finishedlog = BaseAction(self.finishedlog())
        # self.killallapp = BaseAction(self.killallapp)
        # self.killallapp = self.base.killallapp()

    # def test_swipe_to_right(self):
    #     self.page.carcenter.swipe_to_right()
    
    # 测试用例1打开车辆
    @allure.severity(allure.severity_level.BLOCKER)
    def test_01_open_carcenter(self):
        # 首次向右滑动一屏，非首次不动
        # self.page.carcenter.swipe_to_right()
        # home - 点击 车辆
        self.page.carcenter.click_carcenter() 
        # 车辆页面 - 判断 更新状态
        assert "能源管理" == self.page.carcenter.get_carcenter_txt()
        log.info("打开车辆，更新状态断言成功")
    
    # 测试用例2切换车辆左侧Tab栏
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_02_change_carcenter(self):
        
    #     self.page.carcenter.click_carenergy()
        
    #     self.page.carcenter.click_carexperience()
        
    #     self.page.carcenter.click_intelligent_drive()
        
    #     self.page.carcenter.click_carbody()
        
    #     self.page.carcenter.click_carsettings()
        
    #     self.page.carcenter.click_carabout()
    #     log.info("切换车辆Tab栏，更新状态断言成功")
