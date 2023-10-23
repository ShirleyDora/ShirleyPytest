from page.carcenter_page import CarcenterPage

class Page:

    def __init__(self, driver):
        self.driver = driver
    
    @property
    def carcenter(self):
        return CarcenterPage(self.driver)
    
 