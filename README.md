# 电商平台接口自动化测试框架

## 项目简介

本项目是基于 Python + Pytest + Requests 搭建的接口自动化测试框架，主要用于对电商平台核心业务接口进行自动化测试。

框架支持：

- Excel 数据驱动
- 动态参数关联
- HTTP 请求封装
- 接口断言
- 数据库断言
- JSON 数据提取
- Allure 测试报告
- 日志记录

适用于：

- 登录接口
- 用户模块
- 商品模块
- 购物车模块
- 订单模块
- 支付模块

---

# 技术栈

- Python
- Pytest
- Requests
- Jinja2
- MySQL
- Allure
- Logging
- OpenPyXL
- JSON
- Git

---

# 项目结构

```bash
api-auto-test-framework/
│
├── testcases/                # 测试用例
│   └── test_runner.py
│
├── utils/                    # 工具类
│   ├── analyse_case.py
│   ├── asserts.py
│   ├── extractor.py
│   ├── send_request.py
│   ├── excel_utils.py
│   ├── allure_utils.py
│   └── logger_utils.py
│
├── data/                     # 测试数据
│   └── cases.xlsx
│
├── config/                   # 配置文件
│   └── config.yaml
│
├── reports/                  # Allure报告
│
├── logs/                     # 日志文件
│
├── requirements.txt          # 项目依赖
├── run.py                    # 项目入口
├── pytest.ini                # pytest配置
├── README.md
└── .gitignore
