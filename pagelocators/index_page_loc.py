# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

from selenium.webdriver.common.by import By


class IndexPageLoc:
    """ 课堂首页的元素定位表达式 """

    # 课程名称链接(课程名称在测试案例调用元素操作行为时传递)
    class_name_link = (By.XPATH, "//a[text()={}]")

    # 用户头像
    user_head = (By.XPATH, "//a[@id='user']//img")

    # 个人设置
    set_up = (By.XPATH, "//a[text()='个人设置']")


