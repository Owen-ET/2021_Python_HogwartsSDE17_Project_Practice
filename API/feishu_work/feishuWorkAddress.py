#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/04 11:28
# @Author  : zc
# @File    : feishuWorkAddress.py
import requests

from API.feishu_work.base import Base


class FeishuWorkCalendars(Base):





    def get_calendarsList_info(self,calendar_id):
        '''获取日历列表'''

        url = f'{self.baseUrl}{calendar_id}'
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

        url = f'{self.baseUrl}'
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

        url = f'{self.baseUrl}{calendar_id}'
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

        url = f'{self.baseUrl}{calendar_id}'
        # headers = {
        #     'Authorization': f"Bearer {self.get_token()}",
        #     'Content-Type': "application/json; charset=utf-8"
        # }
        r = self.send('DELETE',url).json()
        return r


    def delete_error_calendar_id(self,calendar_err,calendar_id_null):
        '''清除错误日历id'''

        # 查询全部日历
        res_info = self.get_calendarsList_info(calendar_id_null)
        print(res_info)
        # 循环取出所有日历id到数组中
        for i in range(2):
            result = res_info['data']['calendar_list'][i]['calendar_id']
            self.list.append(result)
        # 清除错误日历id
        self.list.remove(calendar_err)
        return self.list[0]