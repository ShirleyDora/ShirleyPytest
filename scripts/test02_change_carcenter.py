import time
import os,sys
sys.path.append(os.getcwd())
import allure
from base.get_logger import GetLogger
from base.base_driver import init_driver
from base.base_action import BaseAction
from page.page import Page

import pytest

# 获取日志入口
log = GetLogger().get_logger()


class TestChangeCarcenter:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        # 等待广告
        time.sleep(5)
        # self.initlog = BaseAction(self.initlog())

    def teardown(self):
        self.driver.quit()
        # self.finishedlog = BaseAction(self.finishedlog())
        # self.killallapp = BaseAction(self.killallapp())
           
    @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.repeat(200) 
    def test_change_carcenter(self):  
        # for i in range(10000): 
        self.page.carcenter.click_carenergy()       
        self.page.carcenter.click_carexperience()     
        self.page.carcenter.click_intelligent_drive()    
        self.page.carcenter.click_carbody()    
        self.page.carcenter.click_carsettings()  
        self.page.carcenter.click_carabout()
        log.info("切换车辆Tab栏，更新状态断言成功")

