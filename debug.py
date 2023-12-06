import allure
import pytest
import os
if __name__ == '__main__':
    pytest.main(['scripts/', '-s', '-v', '--alluredir', './result'])
    #pytest.main(['scripts/', '-s', '-v','--lf', '--alluredir', './result'])
    os.system('allure generate ./result -o ./report --clean')
    os.system("allure open ./report")
