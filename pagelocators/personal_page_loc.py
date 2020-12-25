# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

from selenium.webdriver.common.by import By


class PersonalPageLoc:
    """ 用户个人设置页面各元素定位表达式 """

    # 用户昵称
    user_name = (By.XPATH, "//h1[@class='uc-name']")

