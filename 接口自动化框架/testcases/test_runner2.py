import logging

import pytest
from jinja2 import Template
from utils.analyse_case import analyse_case
from utils.asserts import http_assert, jdbc_assert
from utils.extractor import json_extractor, jdbc_extractor
from utils.send_request import send_http_request
from utils.allure_utils import allure_init
from utils.excel_utils import read_excel




class TestRunner():

    #读测试用例中的全部数据
    data = read_excel()

    #提取后的数据需要初始化一个全局变量来保存
    all = {}

    @pytest.mark.parametrize("case",data)
    def test_case(self,case):
        # 引用全局变量all
        all = self.all

        # 根据all的值渲染case
        case = eval(Template(str(case)).render(all))

        # 初始化allure报告
        allure_init(case)

        # 测试用例的描述信息日志
        logging.info(f"用例ID：{case["id"]} 模块：{case["feature"]} 场景：{case["story"]} 标题：{case["title"]}")

        #解析请求数据
        request_data = analyse_case(case)

        #发起请求，得到响应结果
        res = send_http_request(**request_data)

        #处理HTTP断言
        http_assert(case, res)

        # 数据库断言
        jdbc_assert(case)

        # JSON提取
        json_extractor(case, all, res)

        # 数据库提取
        jdbc_extractor(case, all)