import time
import os,sys
sys.path.append(os.getcwd())
import allure
from base.get_logger import GetLogger
from base.base_driver import init_driver
from page.page import Page
from base.base_action import BaseAction
from base.base_analyze import analyze_data
from selenium.webdriver.common.by import By
import pytest
import allure
# 获取日志入口
log = GetLogger().get_logger()


class TestChangeCarcenter:
    def setup_method(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.base = BaseAction(self.driver)
    def teardown_method(self):
        self.driver.quit()        
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("原始标题")
    def test_click_light(self):  
        allure.dynamic.title("点击灯光")
        self.page.carcenter.click_lighting()
        self.base.screen('点击设置-灯光')
    @allure.title("原始标题")
    def test_click_amb_light_switch_on(self):
        allure.dynamic.title("切换氛围灯")
        amb_light_switch_id="com.voyah.cockpit.vehiclesettings:id/layout_amb_light_switch"
        amb_light_switch_name=By.ID,amb_light_switch_id
        self.base.click(amb_light_switch_name)
        self.base.screen('点击开启氛围灯')
    @allure.title("原始标题")
    def test_click_amb_light_switch_off(self):
        allure.dynamic.title("切换氛围灯")
        amb_light_switch_id="com.voyah.cockpit.vehiclesettings:id/layout_amb_light_switch"
        amb_light_switch_name=By.ID,amb_light_switch_id
        self.base.click(amb_light_switch_name)
        self.base.screen('点击关闭氛围灯')
    @allure.title("原始标题")
    def test_static_effect_settings(self):
        allure.dynamic.title("切换效果设置")
        rb_amb_static_id="com.voyah.cockpit.vehiclesettings:id/rb_amb_static"
        rb_amb_static_name=By.ID,rb_amb_static_id
        self.base.click(rb_amb_static_name)
        self.base.screen('点击切换静态效果')
    @allure.title("原始标题")
    def test_dynamic_effect_settings(self):
        allure.dynamic.title("切换效果设置")
        rb_amb_dynamic_id="com.voyah.cockpit.vehiclesettings:id/rb_amb_dynamic"
        rb_amb_static_name=By.ID,rb_amb_dynamic_id
        self.base.click(rb_amb_static_name)
        self.base.screen('点击切换动态效果')
    # def mode_static_setting(self):
    #    pass