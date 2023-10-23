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

class TestCarcenter:
    def setup_method(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.base = BaseAction(self.driver)
        # 等待广告
        time.sleep(5)
        # self.initlog = BaseAction(self.initlog())
        

    def teardown_method(self):
        self.driver.quit()
        # self.finishedlog = BaseAction(self.finishedlog())
        # self.killallapp = BaseAction(self.killallapp)
        # self.killallapp = self.base.killallapp()

    # def test_swipe_to_right(self):
    #     self.page.carcenter.swipe_to_right()
    
    # 测试用例1打开设置
    @allure.severity(allure.severity_level.BLOCKER)
    # @pytest.mark.parametrize("args", analyze_data("carcenter_page_data", "test_carcenter_page"))
    # def test_open_carcenter(self,args):
    def test_open_carcenter(self):
        # 首次向右滑动一屏，非首次不动
        # self.page.carcenter.swipe_to_right()
        # 解析数据
        # xpath = args["xpath"]
        # title = args["title"]  
        # stepInfo = args["stepInfo"] 
        # screen = args["screen"] 
        # assertText = args["assertText"] 
        # toast = args["toast"]
        # log.info("当前xpath为:%s,title为:%s,stepInfo为:%s,screen:%s,assertText:%s,toast:%s" % (xpath, title, stepInfo,screen,assertText,toast))
        # # home - 点击 设置
        self.page.carcenter.click_carcenter()
        # 车辆页面 - 判断 更新状态
        # try:
        #     # 断言
        #     assert self.page.comment.is_toast_exist(toast)
        # except:
        #     self.page.comment.click_send()
        #     assert self.page.comment.is_toast_exist("Fail")
        assert '我的岚图' == self.page.carcenter.get_carcenter_txt()
        # log.info('Pass,打开设置应用，更新状态断言成功')
        # try:
        #     assert assertText == self.page.carcenter.get_carcenter_txt()
        #     log.info(toastPass)
        # except:
        #     assert self.page.carcenter.is_toast_exist("Fail")
        #     log.info(toastFail)
    