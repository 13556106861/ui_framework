# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

import pytest
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from pageobjects.login_page_operate import LoginPageOperate
from pageobjects.class_page_operate import ClassPageOperate
from testdatas.attend_data import AttendData
from middle_ware.project_log import logger
from pageobjects.index_page_operate import IndexPageOperate


@pytest.mark.smoke
@pytest.mark.usefixtures("over_attend")
class TestDigitAttend:
    """ 数字考勤功能测试 """

    def test_teacher_add_digit_attend(self, teacher_login:WebDriver):
        """
        流程案例：老师角色发起考勤、获取考勤码
        :param teacher_login: fixture返回值，返回已登录老师角色并且打开考勤界面的driver
        :return: None
        """
        driver = teacher_login

        ClassPageOperate(driver).click_add_attend()
        # 数字考勤（点击数字考勤-点击开始考勤）
        ClassPageOperate(driver).start_digit_attend()

        # 获取考勤码
        attend_number = ClassPageOperate(driver).get_attend_number()

        # 将考勤码动态设置为AttendData类的属性
        setattr(AttendData, "attend_number", attend_number)

    def test_student_sign_attend(self, init):
        """
        流程案例：学生角色使用考勤码进行签到
        :param init: fixture返回值，返回已打开课堂派首页的driver
        :return: None
        """
        driver = init

        # 学生账号登录
        LoginPageOperate(driver).login(AttendData().student_login_info["email"], AttendData().student_login_info["password"])
        sleep(5)

        # 首页点击班集名称进入班集
        IndexPageOperate(driver).click_course(AttendData().course_name)

        # 立即签到
        ClassPageOperate(driver).go_to_sign_attend(getattr(AttendData, "attend_number"))

    def test_teacher_end_attend(self, teacher_login:WebDriver):
        """
        断言案例：老师角色获取已签到人数并断言签到人数是否正确，结束考勤
        :param teacher_login: fixture返回值，返回已登录老师角色并且打开考勤界面的driver
        :return: None
        """
        driver = teacher_login

        # 进入iframe
        ClassPageOperate(driver).switch_to_attend_iframe()

        # 获取已签到人数
        signed_number = int(ClassPageOperate(driver).get_count_signed_up())

        # 结束考勤
        ClassPageOperate(driver).end_attend()

        # 断言
        try:
            assert signed_number == 1
        except:
            logger.exception(f"已考勤人数断言失败，错误信息：")
            raise








