#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 16:31
# @Author  : zc
# @File    : mainPage_loc.py
from selenium.webdriver.common.by import By


class MainPageloc:


    # 日历左菜单栏
    left_calendar_loc = (By.CSS_SELECTOR,".nav-items>section:nth-child(3)")
    # 切换到日历页面
