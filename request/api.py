# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

from request.base_data import BaseData
from request.request_handle import RequestsCookie
from middle_ware.project_log import logger
from request.data import Data


class Api:

    def __init__(self):
        self.session = RequestsCookie()

    def login(self, data:dict):
        """
        课堂派登录接口
        :param data: 登录账号(dict类型数据）
        :return: None
        """
        # 拼接完整url
        login_url = self.deal_url(BaseData().api_info["login"])
        # 发起登录请求
        try:
            self.session.send_requests("post", login_url, data=data)
        except:
            logger.exception(f"Conf().api_info['login']接口请求失败，错误信息：")
            raise

    def course_list(self):
        """
        获取课程列表接口
        :return: response object
        """

        # 拼接完整url
        course_list_url = self.deal_url(BaseData().api_info["course_lists"])

        try:
            # 发起获取课程列表请求
            response = self.session.send_requests("get", course_list_url)
        except:
            logger.exception(f"{BaseData().api_info['course_lists']}接口请求失败，错误信息：")
            raise
        else:
            # 获取course_id
            course_id = [item["id"] for item in response.json()["toplists"] if item["coursename"] == 'Renee Brooks'][0]

            # 动态设置course_id为Data类的类属性
            Data.courseid = {"courseid": course_id}

            logger.info(f"设置{course_id}为Data类的courseid类属性值")

    def get_not_finish_attend(self, data):
        """
        获取未完成的考勤
        :param data: courseid（dict类型）
        :return: response object
        """
        # 拼接完整url
        attend_list_url = self.deal_url(BaseData().api_info["getNotFinishAttence"])
        # 发起获取考勤列表的请求
        try:
            response = self.session.send_requests("get", attend_list_url, params=data)
            res = response.json()
        except:
            logger.exception(f"{BaseData().api_info['getNotFinishAttence']}接口请求失败，错误信息：")
            raise
        else:
            if len(res['lists']):
                attend_id = res["lists"][0]["id"]
            else:
                attend_id = False
            Data.id = {"id": attend_id}
            logger.info(f"设置{attend_id}为Data类的id类属性值")

    def over_attend(self, data):
        """
        结束考勤接口
        :param data: attenceid（dict类型）
        :return: response object
        """

        # 拼接完整的url
        over_attend_url = self.deal_url(BaseData().api_info["overattence"])
        # 发起结束考勤请求
        try:
            response = self.session.send_requests("post", over_attend_url, data=data)
        except:
            logger.exception(f"{BaseData().api_info['overattence']}接口请求失败，错误信息：")
            raise
        else:
            if response.json()["info"] == "success":
                logger.info(f"已结束id为：{data['id']}的考勤")

    @staticmethod
    def deal_url(api_url: str):
        """
        拼接完整的url （包含base_url + api_url）
        :param api_url: 接口url
        :return: 完整的url地址
        """

        if api_url.startswith("http://") or api_url.startswith("https://"):
            return api_url
        return f"{BaseData().base_url}{api_url}"


if __name__ == '__main__':

    def over_attenc():
        api = Api()

        # 登录
        api.login(Data().teacher_info)

        # 获取课程id
        api.course_list()

        # 获取考勤id
        api.get_not_finish_attend(Data().courseid)

        # 判断正在考勤的id是否为空（为空表示无正在考勤记录），不为空则调用结束考勤的接口结束考勤
        if Data().courseid:
            api.over_attend(Data().id)

    over_attenc()













