# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

import pytest
from time import sleep
from selenium import webdriver
from pageobjects.login_page_operate import LoginPageOperate
from pageobjects.class_page_operate import ClassPageOperate
from pageobjects.index_page_operate import IndexPageOperate
from testdatas.global_data import GlobalData
from request.api import Api
from request.data import Data


@pytest.fixture
def init():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(GlobalData().log_url)
    sleep(3)
    yield driver
    driver.quit()


@pytest.fixture
def teacher_login(init):
    driver = init
    LoginPageOperate(driver).login(GlobalData().teacher_login_info["email"], GlobalData().teacher_login_info["password"])
    sleep(5)
    # 首页点击班集名称进入班集
    IndexPageOperate(driver).click_course(GlobalData().course_name)
    sleep(5)
    # 班集页面点击考勤
    ClassPageOperate(driver).click_attend()
    sleep(3)
    yield driver


@pytest.fixture(scope="class")
def over_attend():
    api = Api()

    # 登录
    api.login(Data().teacher_info)

    # 获取课程id
    api.course_list()

    # 获取未结束的考勤id
    api.get_not_finish_attend(Data().courseid)

    # 判断未结束的考勤id是否为空，不为空则结束考勤
    if Data().courseid:
        api.over_attend(Data().id)







