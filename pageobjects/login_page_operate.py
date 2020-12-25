# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

from time import sleep
from common.base_page_operate import BasePageOperate
from pagelocators.login_page_loc import LoginPageLoc as loc


class LoginPageOperate(BasePageOperate):
    """ 课堂派登录页面各元素操作 """

    def close_page_window(self):
        """ 关闭登录页面弹窗 """

        self.click_ele(loc.win_close, "登录页面_关闭弹窗")

    def login(self, user_name, pwd):
        """
        登录（默认使用账号登录）
        :param user_name: 登录用户名
        :param pwd: 登录密码
        :return: None
        """

        self.close_page_window()
        sleep(3)

        # 点击登录控件
        self.click_ele(loc.login_button, "登录页面_点击登录")
        sleep(3)
        # 输入用户名与密码
        self.input_value_for_ele(loc.user_name_input, "登录页面_登录窗口_账号登录_输入密码名", user_name)
        self.input_value_for_ele(loc.pwd_input, "登录页面_登录窗口_账号登录_输入密码", pwd)
        # 点击登录
        self.click_ele(loc.login_submit, "登录页面_登录窗口_点击登录")






