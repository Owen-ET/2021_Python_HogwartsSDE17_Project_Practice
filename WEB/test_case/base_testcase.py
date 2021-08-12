#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/12 09:48
# @Author  : zc
# @File    : base_testcase.py


from WEB.page.web import Web
from WEB.test_case.calendar.baseTestData import BaseTestData


class BaseTestCase:

    def setup_class(self):
        print("=======case_class_start=======")
        self.data = BaseTestData()

    def teardown_class(self):
        print("=======case_class_stop=======")

    def setup(self):
        print("=======case_start=======")
        self.web = Web().startWeb(self.data.url)
        self.login = self.web.goto_loginPage()
        self.calendarPage = self.login.goto_mainPage(self.data.mobile).goto_calendarPage()

    def teardown(self):
        print("=======case_stop=======")