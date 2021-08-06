#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/04 17:16
# @Author  : zc
# @File    : testCalendars.py
from API.test_case.base_testcase import BaseTestCase


class TestCalendars(BaseTestCase):


    def test_create_calendars(self):
        res_create = self.calendars.create_calendars(self.data.summary,
                                        self.data.description,
                                        self.data.permissions,
                                        self.data.color,
                                        self.data.summary_alias)
        assert res_create['code'] == 0

        result = self.calendars.get_calendarsList_info(self.calendars.delete_error_calendar_id(self.data.calendar_err,self.data.calendar_id_null))
        assert result['code'] == 0


    def test_get_calendars(self):
        res_get = self.calendars.get_calendarsList_info(self.data.calendar_id_null)
        print(res_get)
        assert res_get['code'] == 0


    def test_update_calendars(self):
        res_update = self.calendars.update_calendars(self.calendar_id,
                                                     self.data.newSummary,
                                                     self.data.description,
                                                     self.data.permissions,
                                                     self.data.color,
                                                     self.data.summary_alias)
        assert res_update['code'] == 0

        res_get = self.calendars.get_calendarsList_info(self.data.calendar_id_null)
        print(res_get)
        assert res_get['code'] == 0


    def test_delete_calendars(self):
        res_delete = self.calendars.delete_calendars(self.calendar_id)
        assert res_delete['code'] == 0

        res_info = self.calendars.get_calendarsList_info(self.calendar_id)
        assert res_info['code'] == 0
        print(res_info)