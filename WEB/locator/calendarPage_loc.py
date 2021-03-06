#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 16:56
# @Author  : zc
# @File    : calendarPage_loc.py

from selenium.webdriver.common.by import By


class CalendarPageLoc:

    # 加号按钮
    plusButton_loc = (By.CSS_SELECTOR,".sidebar-more-trigger")
    # 新建日历按钮
    addCalendarButton_loc = (By.CSS_SELECTOR,"._portal>div>div:nth-child(2)>div")
    # 日历名称
    calendarName_loc = (By.CSS_SELECTOR,".summary-input-adaptive>input")
    # 添加描述
    description_loc = (By.CSS_SELECTOR,"._textarea-adaptive>textarea")
    # 创建日历按钮
    createCalendarButton_loc = (By.CSS_SELECTOR,".larkc-btn")
    # 新日历的名称：第三行
    newCalendarName_loc = (By.CSS_SELECTOR,".choose-calendar>div>.calendars>div:nth-child(2)>.calendar-summary-with-icon>div")
    # 定位元素到日历上
    moveToCalendar_loc = (By.CSS_SELECTOR, ".choose-calendar>div>.calendars>div:nth-child(2)")
    # 删除日历按钮
    deleteCalendarButton_loc = (By.CSS_SELECTOR,".choose-calendar>div>.calendars>div:nth-child(2)>.unfollow")
    # 删除日历确定按钮
    delCalOKButton_loc = (By.CSS_SELECTOR,".uni-btn-theme-primary")
    # 日历设置按钮
    setCalendarButton_loc = (By.CSS_SELECTOR,".choose-calendar>div>.calendars>div:nth-child(2)>.setting")