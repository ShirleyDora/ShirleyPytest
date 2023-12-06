import time
import allure
from base.get_logger import GetLogger
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from base.base_analyze import analyze_data
import pytest
# 获取日志入口
log = GetLogger().get_logger()
class LocalMusicPage(BaseAction):
    localMusicIcon = By.XPATH, "//*[contains(@text,'本地音乐')]"
    @allure.step(title="桌面页-点击本地音乐图标")
    def click_local_music_icon(self):
         log.info("正在点击桌面页的本地音乐图标")
         self.click(self.localMusicIcon)