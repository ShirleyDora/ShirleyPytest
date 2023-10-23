import time
import os,sys
sys.path.append(os.getcwd())
import allure
from base.get_logger import GetLogger
from base.base_driver import init_driver
from page.page import Page
from base.base_action import BaseAction
from base.base_analyze import analyze_data
import pytest
import allure
# 获取日志入口
log = GetLogger().get_logger()
arg = analyze_data("desktop_page_data", "test_desktop_page")

@allure.feature('点击桌面上的图标')
class TestCarcenter:
    def setup_method(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.base = BaseAction(self.driver)
        # 等待广告
        time.sleep(5)     
    def teardown_method(self):
        time.sleep(5)  
        self.driver.quit()
    
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("args", analyze_data("desktop_page_data", "test_desktop_page"))
    def test_click_appicon(self,args):
        # 解析数据
        assertText1 = args["assertText1"]
        assertText2 = args["assertText2"] 
        toastPass = args["toastPass"]
        toastFail = args["toastFail"]
        titleText = args["titleText"]
        screen = args["screen"]
        with allure.step(f'步骤1：{titleText}'):  
            self.base.screen(f'{screen}前')
            self.page.desktop.click_desktopAppicon(args)
        with allure.step("步骤2：点击后"): 
            try:
                assert self.page.desktop.is_toast_exist(assertText1 or assertText2) 
                log.info(toastPass)
                self.base.screen(f'{screen}后')
                self.base.press_home_icon()
            except:
                log.info(toastFail)
                self.base.screen(f'{screen}后')
                time.sleep(5)
                self.base.press_home_icon()
                time.sleep(5)
                assert self.page.desktop.is_toast_exist("Fail")
                

        
