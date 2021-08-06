#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 15:32
# @Author  : zc
# @File    : test_calendar.py
from WEB.page.web import Web


class TestCalendar:


    def setup(self):
        self.web = Web().startWeb()
        self.login = self.web.goto_loginPage()



    def test_login(self):

        self.login.goto_mainPage().goto_calendarPage().createCalendar_action()