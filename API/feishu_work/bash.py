#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/05 09:11
# @Author  : zc
# @File    : bash.py
import requests


class Base:


    def __init__(self):

        self.s = requests.Session()
        self.token = self.get_token()
        self.s.headers = {
            'Authorization': f"Bearer {self.token}",
            'Content-Type': "application/json; charset=utf-8"
        }


    def get_token(self):
        '''获取token'''
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
        params = {
            'app_id': 'cli_a18de0f937f9500d',
            'app_secret': 'nUzgBNrv1sX20ARjI4dXUbVMYsDkUyPp'
        }
        r = self.send('POST',url,data=params).json()
        return r['tenant_access_token']


    def send(self,*args,**kwargs):
        return self.s.request(*args,**kwargs)