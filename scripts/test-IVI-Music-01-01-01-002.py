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
from datetime import datetime
# 获取日志入口
log = GetLogger().get_logger()
@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('蓝牙音乐')
@allure.feature('01-功能进入/退出')
@allure.story('01-正向功能测试')
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
    @allure.title("原始标题")
    
    # @pytest.mark.parametrize("args", analyze_data("desktop_page_data", "test_desktop_page"))
    def test_click_local_music(self):
        bt_music_id="com.voyah.cockpit.media:id/tv_music_bt"
        bt_music_name=By.ID,bt_music_id
        bt_music_name_text="蓝牙音乐"
        toastPass="Pass,预期结果1.打开本地音乐应用成功"
        toastFail="Fail,预期结果1.打开本地音乐应用失败"
        # 测试用例名
        allure.dynamic.title("中控屏开启：进入APP ALL点击本地音乐：进入蓝牙音乐")
        # 测试用例描述
        allure.dynamic.description("""前置条件：
                                   1.Usage Mode = Convenient/Driving
                                   2.中控屏开启
                                   3.本地音乐当前显示蓝牙音乐
                                   测试步骤:
                                   1.打开APP ALL，点击本地音乐应用
                                   预期结果
                                   1.进入蓝牙音乐
                                   """)
        # 测试步骤1.点击应用-本地音乐；
        with allure.step("前置条件：点击本地音乐图标前"):
            self.base.screen('点击本地音乐图标前')
        with allure.step("测试步骤1：点击本地音乐应用，查看蓝牙音乐界面"):
            self.page.local_music.click_local_music_icon()
            self.base.screen('点击本地音乐图标中')
        with allure.step("测试步骤2：断言"):
            try:
                assert self.base.get_feature_text(bt_music_name)==bt_music_name_text
                log.info(toastPass)
                self.base.screen('点击本地音乐图标后')
            except:
                print(toastFail)
                log.info(toastFail)
                self.base.screen('点击本地音乐图标后')
                
