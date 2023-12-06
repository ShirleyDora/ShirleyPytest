import time
import allure
from base.get_logger import GetLogger
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from base.base_analyze import analyze_data
import pytest
# 获取日志入口
log = GetLogger().get_logger()
class SettingsPage(BaseAction):
    settingsIcon = By.XPATH, "//*[contains(@text,'设置')]"
    @allure.step(title="桌面页-点击设置图标")
    def click_settings_icon(self):
         log.info("正在点击桌面页的设置图标")
         self.click(self.settingsIcon)
         self.screen('点击设置图标')