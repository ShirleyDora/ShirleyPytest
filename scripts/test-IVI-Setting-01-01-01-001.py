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
arg = analyze_data("desktop_page_data", "test_desktop_page")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature('车辆名称默认为“岚图”')
class TestCarcenter: 
    # 前置条件：
    # 1.车机上电，中控屏处于开启状态
    # 2.车机系统初始状态
    def setup_method(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.base = BaseAction(self.driver)     
    def teardown_method(self):
        self.driver.quit()
    
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title="步骤1.点击设置应用-我的岚图，查看车机名称")
    # @pytest.mark.parametrize("args", analyze_data("desktop_page_data", "test_desktop_page"))
    def test_click_settings(self):
        id="com.voyah.cockpit.vehiclesettings:id/tv_device_name"
        tv_device_name=By.ID,id
        tv_device_name_text="岚图"
        toastPass="Pass,预期结果1.界面上车机名称默认显示为“岚图”"
        toastFail="Fail,预期结果1.界面上车机名称默认不显示为“岚图”"
        # 步骤1.点击设置应用-我的岚图，查看车机名称；
        self.page.settings.click_settings_icon()
        try:
            # 预期结果1.界面上车机名称默认显示为“岚图”
            assert self.base.get_feature_text(tv_device_name)==tv_device_name_text
            log.info(toastPass)
        except:
            assert toastFail
            log.info(toastFail)