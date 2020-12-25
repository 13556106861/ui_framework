# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

from selenium.webdriver.common.by import By


class LoginPageLoc:
    """ 课堂派登录首页 """

    # 课堂派新版本弹窗提示
    win_close = (By.XPATH, "//a[contains(@class, 'ayui-layer-close layui-layer-close2')]")

    # 课堂派首页【登录】控件
    login_button = (By.XPATH, "//a[@class='login']")

    # 登录窗口用户名输入框
    user_name_input = (By.XPATH, "//input[@name='account']")

    # 登录窗口密码输入框
    pwd_input = (By.XPATH, "//input[@name='pass']")

    # 登录窗口【登录】控件
    login_submit = (By.XPATH, "//div[@class='padding-cont pt-login']//a[@class='btn-btn']")










