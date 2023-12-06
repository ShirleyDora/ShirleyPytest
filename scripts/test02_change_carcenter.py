import time
import os,sys
sys.path.append(os.getcwd())
import allure
from base.get_logger import GetLogger
from base.base_driver import init_driver
from base.base_action import BaseAction
from base.base_analyze import analyze_data
from page.page import Page

import pytest

# 获取日志入口
log = GetLogger().get_logger()


class TestChangeCarcenter:
    def setup_method(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.base = BaseAction(self.driver)
        # 等待广告
        # time.sleep(5)
        # self.initlog = BaseAction(self.initlog())

    def teardown_method(self):
        self.base.press_home_icon()
        self.driver.quit()
        # self.finishedlog = BaseAction(self.finishedlog())
        # self.killallapp = BaseAction(self.killallapp())
           
    @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.repeat(200) 
    def test_change_carcenter(self):  
        # for i in range(10000): 
        # self.page.carcenter.click_itemTab()
        # 点击我的岚图
        self.page.carcenter.click_my_lantu()
        # self.page.carcenter.click_carenergy()      
        # 点击车辆 
        self.page.carcenter.click_vehicle()
        # self.page.carcenter.click_carexperience() 
        # 点击灯光
        self.page.carcenter.click_lighting()    
        # self.page.carcenter.click_intelligent_drive()    
        # 点击驾驶偏好
        self.page.carcenter.click_driving_preferences()
        # self.page.carcenter.click_carbody()   
        # 点击驾驶辅助
        self.page.carcenter.click_driving_assistant()
        # 点击显示
        self.page.carcenter.click_display()  
        # 点击声音
        self.page.carcenter.click_sound()
        # 点击连接
        self.page.carcenter.click_connect()
        # 点击安全维护
        self.page.carcenter.click_security()
        # 点击系统
        self.page.carcenter.click_system()
        log.info("切换车辆Tab栏，更新状态断言成功")

