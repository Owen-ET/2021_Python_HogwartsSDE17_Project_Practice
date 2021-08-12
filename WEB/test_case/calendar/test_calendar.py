#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 15:32
# @Author  : zc
# @File    : test_calendar.py

from WEB.test_case.base_testcase import BaseTestCase


class TestCalendar(BaseTestCase):

    def test_seart_calendar(self):
        """测试用例：查询日历名称"""
        self.calendarName = self.calendarPage.seart_calendarName()
        assert self.calendarName == "", "获取的内容与预想不一致！"

    def test_create_calendar(self):
        """测试用例：创建日历"""

        self.calendarPage.createCalendar_action(self.data.calendarName,self.data.description)
        self.calendarName = self.calendarPage.seart_calendarName()
        assert self.calendarName == "测试日历1","获取的内容与预想不一致！"

    def test_delete_calendar(self):
        """测试用例：删除日历"""
        self.calendarPage.createCalendar_action(self.data.calendarName,self.data.description)
        self.calendarName = self.calendarPage.seart_calendarName()
        assert self.calendarName == "测试日历1", "第一个：获取的内容与预想不一致！"

        self.calendarPage.deleteCalendar_action()
        self.calendarName = self.calendarPage.seart_calendarName()
        assert self.calendarName == "", "第二个：获取的内容与预想不一致！"

    def test_update_calendar(self):
        """测试用例：更新日历"""
        self.calendarPage.createCalendar_action(self.data.calendarName,self.data.description)
        self.calendarName = self.calendarPage.seart_calendarName()
        assert self.calendarName == "测试日历1", "第一个：获取的内容与预想不一致！"

        self.calendarPage.updateCalendar_action(self.data.updateCalendarName)
        self.calendarName = self.calendarPage.seart_calendarName()
        assert self.calendarName == "测试日历2", "第二个：获取的内容与预想不一致！"

        self.calendarPage.deleteCalendar_action()
        self.calendarName = self.calendarPage.seart_calendarName()
        assert self.calendarName == "", "第三个：获取的内容与预想不一致！"