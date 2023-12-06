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
    @allure.severity(allure.severity_level.NORMAL)        
    # @allure.step(title="步骤1.点击蓝牙音乐的暂停按钮")
    @allure.title("原始标题")
    def test_click_bt_music_pause(self):
        # 停止按钮
        pause_bt_music_button="com.voyah.cockpit.media:id/iv_bt_pause"
        pause_bt_music_button_id=By.ID,pause_bt_music_button
        # 音乐播放的进度条时间点
        bt_music_ongoing_time="com.voyah.cockpit.media:id/tv_start_time"
        bt_music_ongoing_time_id=By.ID,bt_music_ongoing_time
        # 测试用例名
        allure.dynamic.title("点击蓝牙音乐的暂停按钮，暂停蓝牙音乐")
        # 测试用例描述
        allure.dynamic.description("""前置条件：
                                   1.车机上电，中控屏处于开启状态
                                   2.车机系统初始状态
                                   测试步骤：
                                   1.从桌面页点击打开本地音乐应用 
                                   2.点击蓝牙音乐的暂停按钮 
                                   预期结果：
                                   1.可以正常打开本地音乐，本地音乐界面显示正常 
                                   2.可以暂停蓝牙音乐
                                   """)
        toastPass="Pass,预期结果1.已暂停蓝牙音乐播放"
        toastFail="Fail,预期结果1.暂停蓝牙音乐失败，还在继续播放中"
        with allure.step("前置条件：点击暂停蓝牙音乐前"):
            self.base.screen('点击暂停蓝牙音乐前')
        with allure.step("测试步骤1：点击暂停蓝牙音乐中"):
            self.base.click(pause_bt_music_button_id)
            self.base.screen('点击暂停蓝牙音乐中')
            time.sleep(1)
        with allure.step("测试步骤2：断言"):
            try:
                 self.base.screen('已点击暂停按钮')
                 bt_music_ongoing_time1=self.base.get_feature_text(bt_music_ongoing_time_id)
                 time.sleep(1)
                 bt_music_ongoing_time2=self.base.get_feature_text(bt_music_ongoing_time_id)
                 log.info('{},{}'.format(bt_music_ongoing_time1,bt_music_ongoing_time2))
                 assert bt_music_ongoing_time2==bt_music_ongoing_time1,toastFail
                 self.base.screen("等待后音乐界面状态")
                 log.info(toastPass)
            except:
                 log.info(toastFail)
                 self.base.screen('暂停蓝牙音乐失败')
                 assert False