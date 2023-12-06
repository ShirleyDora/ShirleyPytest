from page.carcenter_page import CarcenterPage
from page.desktop_page import DesktopPage
from page.settings_page import SettingsPage
from page.music_page import LocalMusicPage
class Page:

    def __init__(self, driver):
        self.driver = driver
    
    @property
    def carcenter(self):
        return CarcenterPage(self.driver)
    @property
    def desktop(self):
        return DesktopPage(self.driver)
    @property
    def settings(self):
        return SettingsPage(self.driver)
    @property
    def local_music(self):
        return LocalMusicPage(self.driver)
    
    
 