# 电商平台接口自动化测试框架

## 项目介绍

基于 Python + Pytest + Requests 搭建的接口自动化测试框架。

支持：

- Excel 数据驱动
- 动态参数关联
- HTTP 请求封装
- 数据库断言
- JSON 数据提取
- Allure 测试报告

---

## 技术栈

- Python
- Pytest
- Requests
- Jinja2
- MySQL
- Allure

---

## 项目结构

```bash
testcases/
utils/
data/
config/
```

---

## 运行方式

安装依赖：

```bash
pip install -r requirements.txt
```

执行测试：

```bash
pytest
```

生成 Allure 报告：

```bash
allure serve reports/
```
