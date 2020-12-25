# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

from testdatas.global_data import GlobalData


class Data(GlobalData):

    @property
    def teacher_info(self):
        """
        老师角色登录账号
        :return:
        """
        self.teacher_login_info["remember"] = 0
        teacher_info = self.teacher_login_info

        return teacher_info

    # 课程id
    courseid = None

    # 考勤id
    id = None









