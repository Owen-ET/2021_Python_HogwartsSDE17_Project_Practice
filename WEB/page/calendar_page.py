#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 16:52
# @Author  : zc
# @File    : calendar_page.py
from WEB.page.base_page import Base
from WEB.locator.calendarPage_loc import CalendarPageLoc as loc


class CalendarPage(Base):
    """日历页面"""

    def createCalendar_action(self):
        """创建日历操作"""
        self.el_click(loc.plusButton_loc)
        self.el_click(loc.addCalendarButton_loc)
        self.el_sendKeys(loc.calendarName_loc,"测试日历1")
        self.el_sendKeys(loc.description_loc,"测试日历描述1")
        self.el_click(loc.createCalendarButton_loc)


    # def deleteCalendar_action(self):
    #     """删除日历操作"""

