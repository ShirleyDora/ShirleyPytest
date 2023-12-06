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
        self.base.press_home_icon()
        self.driver.quit()
    @allure.severity(allure.severity_level.NORMAL)   
    @allure.title("原始标题")
    # @allure.step(title="步骤1.点击蓝牙音乐的切换下一首按钮")
    def test_click_bt_music_change_next_music(self):
        # 下一首按钮
        next_bt_music_button="com.voyah.cockpit.media:id/iv_bt_next"
        next_bt_music_button_id=By.ID,next_bt_music_button
        # 蓝牙音乐名字
        bt_music_title="com.voyah.cockpit.media:id/tv_music_title"
        bt_music_title_id=By.ID,bt_music_title
        # 测试用例名
        allure.dynamic.title("点击蓝牙音乐的切换下一首按钮，切换下一首蓝牙音乐")
        # 测试用例描述
        allure.dynamic.description("""前置条件：
                                   1.车机上电，中控屏处于开启状态
                                   2.车机系统初始状态
                                   测试步骤：
                                   1.从桌面页点击打开本地音乐应用 
                                   2.点击蓝牙音乐的切换下一首按钮
                                   预期结果：
                                   1.可以正常打开本地音乐，本地音乐界面显示正常 
                                   2.可以切换下一首蓝牙音乐
                                   """)
        toastPass="Pass,预期结果1.已切换下一首蓝牙音乐"
        toastFail="Fail,预期结果1.切换下一首蓝牙音乐失败"
        self.base.screen('点击切换下一首蓝牙音乐前')
        bt_music_title_name1=self.base.get_feature_text(bt_music_title_id)
        self.base.click(next_bt_music_button_id)
        time.sleep(5)
        try:
             bt_music_title_name2=self.base.get_feature_text(bt_music_title_id)
            #  assert 实际=预期，错误信息
             assert bt_music_title_name2!=bt_music_title_name1
             self.base.screen("已切换下一首蓝牙音乐")
             log.info(toastPass)
        except:
             print(toastFail)
             log.info(toastFail)
             self.base.screen('切换下一首蓝牙音乐失败')