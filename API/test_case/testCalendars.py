#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/04 17:16
# @Author  : zc
# @File    : testCalendars.py
from API.feishu_work.feishuWorkAddress import FeishuWorkCalendars


class TestCalendars:


    def setup_class(self):
        self.list = []
        self.summary = '测试日历5'
        self.newSummary = '更改测试日历5'
        self.description = '测试日历描述5'
        self.permissions = 'public'
        self.color = -1
        self.summary_alias = '测试日历备注名5'
        self.calendar_id = 'feishu.cn_V03mp6MHH4VBQNjuZdfYEc@group.calendar.feishu.cn'
        self.calendar_err = 'feishu.cn_CLVH6pnyg9wzyMBKeaC9Ed@group.calendar.feishu.cn'
        self.calendar_id_null = ''
        self.calendars = FeishuWorkCalendars()



    def test_create_calendars(self):
        res_create = self.calendars.create_calendars(self.summary,
                                        self.description,
                                        self.permissions,
                                        self.color,
                                        self.summary_alias)
        assert res_create['code'] == 0

        res_info = self.calendars.get_calendarsList_info(self.calendar_id_null)
        print(res_info)
        for i in range(2):
            result = res_info['data']['calendar_list'][i]['calendar_id']
            self.list.append(result)
        self.list.remove(self.calendar_err)
        result = self.calendars.get_calendarsList_info(self.list[0])
        assert result['code'] == 0


    def test_get_calendars(self):
        res_get = self.calendars.get_calendarsList_info(self.calendar_id_null)
        print(res_get)
        assert res_get['code'] == 0


    def test_update_calendars(self):
        res_update = self.calendars.update_calendars(self.calendar_id,
                                                     self.newSummary,
                                                     self.description,
                                                     self.permissions,
                                                     self.color,
                                                     self.summary_alias)
        assert res_update['code'] == 0


    def test_delete_calendars(self):
        res_info = self.calendars.get_calendarsList_info(self.calendar_id)
        assert res_info['code'] == 0

        res_delete = self.calendars.delete_calendars(self.calendar_id)
        assert res_delete['code'] == 0
