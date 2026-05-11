import os

import pytest

if __name__ == "__main__":
    pytest.main(["-vs", "./testcases/test_runner2.py","--alluredir","./report/json_test","--clean-alluredir"])
    os.system("allure generate ./report/json_test -o ./report/html_test --clean")