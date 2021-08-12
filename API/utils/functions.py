#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/05 10:40
# @Author  : zc
# @File    : functions.py

import os
import yaml


class Functions:

    def upPath(self):
        '''获取上级目录路径'''
        basePath = os.path.dirname(os.path.dirname(__file__))
        return basePath


    def getYamlData(self,yamlName):
        '''获取yaml数据'''
        yamlPath = self.upPath() + f'/data/{yamlName}Data.yaml'
        with open(yamlPath,encoding='utf-8') as file:
            data = yaml.load(file)
        return data[yamlName]