#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 09:32
# @Author  : zc
# @File    : base_testcase.py
from API.feishu_work.calendar_api.feishuWorkAddress import FeishuWorkCalendars
from API.test_case.calendar.baseCalendarsTestData import BaseCalendarsTestData


class BaseTestCase:

    def setup_class(self):
        self.data = BaseCalendarsTestData()
        self.calendars = FeishuWorkCalendars()


    def setup(self):

        print("=======case_start=======")
        try:
            self.calendar_id = self.calendars.delete_error_calendar_id(self.data.calendar_err,self.data.calendar_id_null)
        except:
            pass


    def teardown(self):
        print("=======case_stop=======")