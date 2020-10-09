# !/usr/bin/env python
# -*- coding:utf8 -*-

import os
import csv
import time
import random

import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

# 考试城市、日期
CITY = "北京"
DATE = "2020-01-04"

# 托福账号、密码
USERNAME_TF = "8079054"
PASSWORD_TF = "Aa591465908"

class GetToeflTestInfos():
    def __init__(self):
        self.username = USERNAME_TF
        self.password = PASSWORD_TF
        self.index_url = "https://toefl.neea.cn/index"
        self.option = webdriver.FirefoxOptions()
        self.option.add_argument('--user-agent="Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"')
        # self.option.add_argument('--headless')    # 启用无界面模式，爬取的时候不会弹出浏览器
        self.driver = webdriver.Firefox(options=self.option)
        self.wait = WebDriverWait(self.driver, timeout=30)
