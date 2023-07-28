import allure
import pytest
import os
if __name__ == '__main__':
    pytest.main(['scripts/test02_change_carcenter.py', '-s', '-v', '--alluredir', './result'])
    os.system('allure generate ./result -o ./report --clean')
    os.system("allure open ./report")
