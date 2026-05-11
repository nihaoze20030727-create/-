import logging

import allure
import jsonpath

from utils.send_request import send_jdbc_request

@allure.step("http响应断言")
def http_assert(case, res):
    if case["check"]:
        result = jsonpath.jsonpath(res.json(), case["check"])[0]
        logging.info(f"HTTP响应断言内容是：实际结果({result}) == 预期结果({case["expected"]})")
        assert result == case["expected"]
    else:
        logging.info(f"HTTP响应断言内容是：实际结果({case['expected']}) in 响应结果({res.text})")
        assert case["expected"] in res.text


def jdbc_assert(case):
    if case["sql_check"] and case["sql_expected"]:
        with allure.step("jdbc响应断言"):
            result = send_jdbc_request(case["sql_check"])
            logging.info(f"JDBC响应断言内容是：实际结果({result}) in 响应结果({case["sql_expected"]})")
            assert send_jdbc_request(case["sql_check"]) == case["sql_expected"]