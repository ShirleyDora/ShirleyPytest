import time
import os,sys
sys.path.append(os.getcwd())
import allure
from base.get_logger import GetLogger
from base.base_action import BaseAction
from base.base_analyze import analyze_data
import pytest
from selenium.webdriver.common.by import By
# 获取日志入口
log = GetLogger().get_logger()

class DesktopPage(BaseAction):
    def setup_method(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        # 等待广告
        time.sleep(5)
    def click_desktopAppicon(self,args):
         # 解析数据
        xpath = args["xpath"]
        stepInfo = args["stepInfo"] 
        screen = args["screen"] 
        titleText = args["titleText"]
        desktopAppicon = By.XPATH,xpath  
        log.info(stepInfo)
        self.click(desktopAppicon)


    # 获取页面状态    
    # def get_assert_txt(self,args):
    #     assertText1 = args["assertText1"]
    #     assertText2 = args["assertText2"] 
    #     assertText3 = By.XPATH, "//*[contains(@text,{assertText1})]"
    #     assertText4 = By.XPATH, "//*[contains(@text,{assertText2})]"
    #     log.info("正在获取获取详情页面状态")
    #     self.screen('查看详情页面状态')
    #     print('3')
    #     log.info("3")
    #     print(assertText3)
    #     return self.get_feature_text(assertText3)