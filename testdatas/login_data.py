# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe


from testdatas.global_data import GlobalData


class LoginData(GlobalData):
    """ 登录测试数据 """

    # 老师账号 + 昵称
    @property
    def teacher_info(self):
        self.teacher_login_info["nickname"] = "IDO"
        teacher_info = self.teacher_login_info

        return teacher_info

    # 学生账号 + 昵称
    @property
    def student_info(self):
        self.student_login_info["nickname"] = "Simple_Small"
        student_info = self.student_login_info

        return student_info


if __name__ == '__main__':
    print([LoginData().teacher_info, LoginData().student_info])