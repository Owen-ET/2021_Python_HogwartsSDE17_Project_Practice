#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 13:46
# @Author  : zc
# @File    : functions.py
import os


class Functions:

    def curPath(self):
        """获取上层目录"""
        basePath = os.path.dirname(os.path.abspath(__file__))
        return basePath