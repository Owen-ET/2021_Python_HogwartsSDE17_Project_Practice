#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 15:52
# @Author  : zc
# @File    : loginPage_loc.py
from selenium.webdriver.common.by import By


class LoginPageLoc:

    # 手机号
    mobile_loc = (By.CSS_SELECTOR,".mobile-input-phone")
    # 单选框
    checkBox_loc = (By.CSS_SELECTOR, ".base-check-box")
    # 下一步按钮
    nextButton_loc = (By.CSS_SELECTOR,".base-button-primary")
    # 进入按钮
    enterButton_loc = (By.CSS_SELECTOR,".open-list-part>div:nth-child(2)>div:nth-child(3)>div")