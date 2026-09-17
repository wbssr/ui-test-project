# SauceDemo UI 自动化测试框架

## 项目简介

基于 Selenium + pytest + Page Object 模式的 UI 自动化测试框架，被测系统为 SauceDemo 电商网站。

覆盖登录、商品、购物车、结算 4 个核心模块，包含正向流程、异常场景和边界条件。

## 技术栈

| 模块 | 技术 |
| :--- | :--- |
| UI 自动化 | Selenium |
| 测试框架 | pytest |
| 设计模式 | Page Object |
| 数据驱动 | JSON + pytest 参数化 |
| 等待机制 | 显式等待封装 |
| 日志 | logging（控制台 + 文件） |
| 测试报告 | Allure |
| 失败截图 | 自动截图保存 |

## 项目结构
```
ui-test-project/
├── pages/
│   ├── base_page.py           # 基础页面封装
│   ├── login_page.py          # 登录页
│   ├── inventory_page.py      # 商品列表页
│   ├── cart_page.py           # 购物车页
│   └── checkout_page.py       # 结算页
├── tests/
│   ├── conftest.py            # 浏览器 fixture + 失败截图
│   ├── test_login.py          # 登录测试（数据驱动）
│   ├── test_inventory.py      # 商品测试
│   ├── test_cart.py           # 购物车测试
│   └── test_checkout.py       # 结算测试
├── config/
│   ├── settings.py            # 全局配置
│   └── test_data/
│       └── users.json         # 用户测试数据
├── utils/
│   └── logger.py              # 日志模块
│   └── data_loader.py         # 数据加载
├── screenshots/               # 失败截图
├── logs/                      # 日志文件
├── reports/                   # Allure 报告
├── pytest.ini
├── requirements.txt
└── README.md
```
## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```
### 2. 运行测试
#### 全部测试
```bash
pytest tests/ -v
```
#### 冒烟测试
```bash
pytest tests/ -m smoke -v
```
#### 回归测试
```bash
pytest tests/ -m regression -v
```
#### 生成 Allure 报告
```bash
pytest tests/ -v --alluredir=reports/allure-results
allure serve reports/allure-results
```
## 测试覆盖
| 模块 | 用例数 | 覆盖内容 |
| :--- | :--- | :--- |
| 登录 | 6 | 多用户登录、错误密码、空用户名、空密码、锁定用户 |
| 商品 | 3 | 排序、页面标题、多商品添加 |
| 购物车 | 2 | 添加移除、空购物车 |
| 结算 | 3 | 完整流程、缺信息、完成页 |
| 总计 | 14 | |
## 核心特性
- Page Object 分层，页面操作与测试逻辑分离

- 数据驱动：users.json + pytest 参数化

- 显式等待封装，避免硬编码 sleep

- 失败自动截图，便于问题定位

- 日志双输出：控制台 + 文件

- pytest 标记区分冒烟和回归

- Allure 可视化报告

### CI/CD

项目配置了 GitHub Actions，代码提交后自动运行 UI 测试。

- 自动安装 Chrome 浏览器
- 自动安装 Python 依赖
- 在 headless 模式下执行全部 UI 测试用例
## 作者
luoqing