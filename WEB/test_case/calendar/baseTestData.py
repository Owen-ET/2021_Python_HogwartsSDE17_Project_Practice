#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/12 10:00
# @Author  : zc
# @File    : baseTestData.py

from WEB.utils.functions import Functions


class BaseTestData:

    loginData = Functions().getYamlData('login')
    calendarData = Functions().getYamlData('calendar')

    # 飞书地址
    url = loginData['url']
    # 手机号
    mobile = loginData['mobile']
    # 日历名称
    calendarName = calendarData['calendarName']
    # 更新日历名称
    updateCalendarName = calendarData['updateCalendarName']
    # 日历描述
    description = calendarData['description']