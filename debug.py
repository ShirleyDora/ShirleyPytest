import allure
import pytest
import os
if __name__ == '__main__':
    # pytest.main(['scripts/test03_click_appicon.py', '-s', '-v'])
    pytest.main(['scripts/test03_click_appicon.py', '-s', '-v', '--alluredir', './result'])
    os.system('allure generate ./result -o ./report --clean')
    os.system("allure open ./report")
