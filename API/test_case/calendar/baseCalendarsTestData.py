#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 10:22
# @Author  : zc
# @File    : baseCalendarsTestData.py
from API.utils.functions import Functions


class BaseCalendarsTestData(Functions):
    baseData = Functions().getYamlData('calendars')

    summary = baseData['summary']
    newSummary = baseData['newSummary']
    description = baseData['description']
    permissions = baseData['permissions']
    color = baseData['color']
    summary_alias = baseData['summary_alias']
    calendar_err = baseData['calendar_err']
    calendar_id_null = baseData['calendar_id_null']