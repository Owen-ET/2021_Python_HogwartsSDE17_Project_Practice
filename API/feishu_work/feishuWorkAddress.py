#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/04 11:28
# @Author  : zc
# @File    : feishuWorkAddress.py
import requests

from API.feishu_work.bash import Base


class FeishuWorkCalendars(Base):





    def get_calendarsList_info(self,calendar_id):
        '''获取日历列表'''
        url = f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}'
        # print(self.get_token())

        # headers = {
        #     'Authorization': f"Bearer {self.get_token()}",
        #     'Content-Type': "application/json; charset=utf-8"
        # }


        # r = self.s.get(url).json()
        r = self.send('GET',url).json()
        return r


    def create_calendars(self,summary,description,permissions,color,summary_alias):
        '''创建日历'''
        url = 'https://open.feishu.cn/open-apis/calendar/v4/calendars'
        # headers = {
        #     'Authorization': f"Bearer {self.get_token()}",
        #     'Content-Type': "application/json; charset=utf-8"
        # }
        data = {
            'summary': summary,
            'description': description,
            'permissions': permissions,
            'color': color,
            'summary_alias': summary_alias
        }

        r = self.send('POST',url,json=data).json()
        return r


    def update_calendars(self,calendar_id,summary,description,permissions,color,summary_alias):
        '''修改日历'''
        url = f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}'

        # headers = {
        #     'Authorization': f"Bearer {self.get_token()}",
        #     'Content-Type': "application/json; charset=utf-8"
        # }
        data = {
            'summary': summary,
            'description': description,
            'permissions': permissions,
            'color': color,
            'summary_alias': summary_alias
        }

        r = self.send('PATCH',url, json=data).json()
        return r


    def delete_calendars(self,calendar_id):
        '''删除日历'''
        url = f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}'
        # headers = {
        #     'Authorization': f"Bearer {self.get_token()}",
        #     'Content-Type': "application/json; charset=utf-8"
        # }
        r = self.send('DELETE',url).json()
        return r