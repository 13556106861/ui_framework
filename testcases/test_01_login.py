# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

import pytest
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from pageobjects.login_page_operate import LoginPageOperate
from pageobjects.personal_page_operate import PersonalPageOperate
from testdatas.login_data import LoginData
from middle_ware.project_log import logger
from pageobjects.index_page_operate import IndexPageOperate


@pytest.mark.regression
@pytest.mark.smoke
class TestLogin:
    """ 登录功能测试 """

    @pytest.mark.parametrize("case", [LoginData().teacher_info, LoginData().student_info])
    def test_login_success(self, case, init:WebDriver):
        driver = init

        # 登录
        LoginPageOperate(driver).login(case["email"], case["password"])
        sleep(5)

        # 点击用户头像
        IndexPageOperate(driver).click_head_img()
        # 点击个人设置
        IndexPageOperate(driver).click_personal_set()
        sleep(3)

        # 断言
        try:
            # 获取昵称并断言
            assert PersonalPageOperate(driver).get_user_nickname() == case["nickname"]
        except:
            logger.exception(f"测试案例执行失败！错误信息：")
            raise


# if __name__ == '__main__':
#     print([LoginData().teacher_info, LoginData().student_info])



