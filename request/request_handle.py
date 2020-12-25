# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

import requests
from middle_ware.project_log import logger


class RequestsCookie:

    """ 此类中的请求方法只适用于cookie鉴权机制的接口请求，
       使用session会话对象发起请求时，一旦服务器生成了cookie，
       session会话对象会绑定该cookie，后续使用session会话对象
       发起请求时会自动带上cookie，无须再传递cookie参数   """

    def __init__(self):
        """ 创建会话 """
        self.session = requests.Session()

    def send_requests(self, method, url, params=None, json=None, data=None, **kw) -> object:
        """
        发起请求（可发起各种方法的请求）
        :param method: 请求方法
        :param url: 请求地址
        :param params: get请求参数
        :param json: post请求数据 （接口必须支持application/json数据格式）
        :param data: post请求数据 （接口必须支持application/x-www-form-urlencoded数据格式）
        :param kw: 其它关键字参数（如：haeders等）
        :return: class:`Response <Response>` object
        """
        logger.info(f"请求url：{url}")
        logger.info(f"请求方法：{method}")

        if method.upper() == "GET":
            logger.info(f"请求数据：{params}")
            return self.session.request("get", url, params=params, **kw)
        elif method.upper() == "POST":
            logger.info(f"请求数据：{data if json is None else json}")
            return self.session.request("post", url, json=json, data=data, **kw)
        else:
            return self.session.request(method, url, json=json, data=data, **kw)

    def close_session(self):
        # 关闭会话
        self.session.close()


class RequestHandle:

    def send_requests(self, method, url, params=None, json=None, data=None, **kw) -> object:
        """
        发起请求（可发起各种方法的请求）
        :param method: 请求方法
        :param url: 请求地址
        :param params: get请求参数
        :param json: post请求数据
        :param data: post请求数据
        :param kw: 其它参数（如：cookies,headers等)
        :return:
        """
        if method.upper() == "GET":
            return requests.get(url, params=params, **kw)
        elif method.upper() == "POST":
            return requests.post(url, json=json, data=data, **kw)
        else:
            return requests.request(method, url, json=json, data=data, **kw)



