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
    def setup_method(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.base = BaseAction(self.driver)    
    def teardown_method(self):
        self.driver.quit()
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("原始标题")
    def test_change_tab_bt_music(self):
        # 左侧Tab栏蓝牙音乐
        bt_music_id="com.voyah.cockpit.media:id/tv_music_bt"
        bt_music_name=By.ID,bt_music_id
        # 右侧Content蓝牙音乐内容
        content_bt_music_id="com.voyah.cockpit.media:id/ll_bluetooth_music"
        content_bt_music_name=By.ID,content_bt_music_id
        # 测试用例名
        allure.dynamic.title("切换本地音乐应用的Tab栏，切换到蓝牙音乐")
        # 测试用例描述
        allure.dynamic.description("""前置条件：
                                   1.车机上电，中控屏处于开启状态
                                   2.车机系统初始状态
                                   测试步骤：
                                   1.从桌面页点击打开本地音乐应用 
                                   2.点击切换Tab栏蓝牙音乐 
                                   预期结果：
                                   1.可以正常打开本地音乐，本地音乐界面显示正常 
                                   2.可以切换蓝牙音乐Tab栏 
                                   """)
        toastPass="Pass,预期结果1.切换蓝牙音乐Tab栏成功"
        toastFail="Fail,预期结果1.切换蓝牙音乐Tab栏失败"
        with allure.step("前置条件：点击切换Tab栏蓝牙音乐前"):
            self.base.screen('点击切换Tab栏蓝牙音乐前')
        with allure.step("测试步骤1：点击切换Tab栏蓝牙音乐中"):   
            self.base.click(bt_music_name)
            self.base.screen('点击切换Tab栏USB音乐中')
        with allure.step("测试步骤2：断言"):
            try:
                assert self.base.find_element(content_bt_music_name)
                self.base.screen("切换蓝牙音乐Tab栏成功")
                log.info(toastPass)
            except:
                print(toastFail)
                log.info(toastFail)
                self.base.screen('切换蓝牙音乐Tab栏失败')
