#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 16:56
# @Author  : zc
# @File    : calendarPage_loc.py
from selenium.webdriver.common.by import By


class CalendarPageLoc:


    # 加号按钮
    plusButton_loc = (By.CSS_SELECTOR,".sidebar-more-trigger")
    # 新增日历按钮
    addCalendarButton_loc = (By.CSS_SELECTOR,"._portal>div>div:nth-child(2)>div")
    # 日历名称
    calendarName_loc = (By.CSS_SELECTOR,".summary-input-adaptive>input")
    # 添加描述
    description_loc = (By.CSS_SELECTOR,"._textarea-adaptive>textarea")
    # 创建日历按钮
    createCalendarButton_loc = (By.CSS_SELECTOR,".larkc-btn")