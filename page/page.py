from page.carcenter_page import CarcenterPage
from page.desktop_page import DesktopPage
class Page:

    def __init__(self, driver):
        self.driver = driver
    
    @property
    def carcenter(self):
        return CarcenterPage(self.driver)
    @property
    def desktop(self):
        return DesktopPage(self.driver)
    
    
 