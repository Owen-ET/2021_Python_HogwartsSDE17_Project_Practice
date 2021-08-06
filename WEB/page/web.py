#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 13:41
# @Author  : zc
# @File    : web.py

from selenium import webdriver

from WEB.page.login_page import LoginPage
from WEB.utils.functions import Functions


class Web:

    def startWeb(self):
        """开启web自动化"""
        self.driver = webdriver.Chrome(Functions().curPath()+"/chromedriver")
        self.driver.get("https://www.feishu.cn/create/?from=calendar_banner_free_register&app_id=11")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self


    def stopWeb(self):
        """关闭浏览器"""
        self.driver.quit()


    def goto_loginPage(self):
        """跳转登录页"""
        return LoginPage(self.driver)