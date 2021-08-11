#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 15:32
# @Author  : zc
# @File    : test_calendar.py
from WEB.page.web import Web


class TestCalendar:


    def setup(self):
        print("=======case_start=======")
        self.web = Web().startWeb()
        self.login = self.web.goto_loginPage()
        self.calendarPage = self.login.goto_mainPage().goto_calendarPage()


    def teardown(self):
        print("=======case_stop=======")


    def test_seart_calendar(self):
        """测试用例：查询日历名称"""
        self.calendarName = self.calendarPage.seart_calendarName()
        assert self.calendarName == "测试日历1", "获取的内容与预想不一致！"


    def test_create_calendar(self):
        """测试用例：创建日历"""

        self.calendarPage.createCalendar_action()
        self.calendarName = self.calendarPage.seart_calendarName()
        assert self.calendarName == "测试日历1","获取的内容与预想不一致！"


    def test_delete_calendar(self):
        """测试用例：删除日历"""
        self.calendarPage.createCalendar_action()
        self.calendarName = self.calendarPage.seart_calendarName()
        assert self.calendarName == "测试日历1", "第一个：获取的内容与预想不一致！"

        self.calendarPage.deleteCalendar_action()
        self.calendarName = self.calendarPage.seart_calendarName()
        assert self.calendarName == "", "第二个：获取的内容与预想不一致！"


    def test_update_calendar(self):
        """测试用例：更新日历"""
        self.calendarPage.createCalendar_action()
        self.calendarName = self.calendarPage.seart_calendarName()
        assert self.calendarName == "测试日历1", "第一个：获取的内容与预想不一致！"

        self.calendarPage.updateCalendar_action()
        self.calendarPage.deleteCalendar_action()