# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

from time import sleep
from common.base_page_operate import BasePageOperate
from pagelocators.class_page_loc import ClassPageLoc as loc


class ClassPageOperate(BasePageOperate):
    """ 班集各元素操作 """

    """ ------- 老师角色 ------- """

    def click_attend(self):
        """
        班集页面_点击【考勤】_弹出考勤弹窗
        :return: None
        """

        self.click_ele(loc.attend_button, "班集页面_点击考勤")

    def switch_to_attend_iframe(self):
        """
        切换进入考勤iframe内
        :return: None
        """

        self.switch_to_iframe(loc.attend_iframe, "班集页面_切换进入考勤iframe")

    def click_add_attend(self):
        """
        考勤弹窗_点击【新建考勤】_弹出新建考勤弹框
        注意：新建考勤元素在iframe内
        :return: None
        """
        self.switch_to_attend_iframe()

        self.click_ele(loc.add_attend, "班集页面_考勤弹窗_点击新建考勤")

    def start_digit_attend(self):
        """
        数字考勤：
        :return: None
        """

        # 新建考勤弹框_点击【数字考勤】
        self.click_ele(loc.digit_attend, "班集页面_考勤弹窗_新建考勤弹框_点击数字考勤")
        # 新建考勤弹框_点击【开始考勤】
        self.start_attend()

    def start_attend(self):
        """
        新建考勤弹窗_开始考勤
        :return: None
        """

        self.click_ele(loc.start_attend, "班集页面_考勤弹窗_新建考勤弹框_点击开始考勤")

    def get_attend_number(self):
        """
        获取考勤码
        :return: 考勤码
        """

        # 获取考勤码所在元素（4个span元素）
        eles = self.get_elements(loc.attend_number, "班集页面_考勤弹窗_考勤窗口_获取考勤码")
        # 获取考勤码
        attend_number = "".join([str(self.get_element_text(ele, "班集页面_考勤弹窗_考勤窗口_获取1位考勤数字")) for ele in eles])

        return attend_number

    def get_count_signed_up(self):
        """
        获取已考勤的人数
        :return: 考勤人数
        """

        return self.get_element_text(loc.signed_up_count, "班集页面_考勤弹窗_考勤窗口_获取已考勤人数")

    def end_attend(self):
        """
        结束考勤
        :return:  None
        """

        # 点击结束考勤
        self.click_ele(loc.end_attend_button, "班集页面_考勤弹窗_考勤窗口_结束考勤")
        # 确认结束考勤
        self.click_ele(loc.sure_end_attend_butten, "班集页面_考勤弹窗_考勤窗口_结束并完成考勤弹窗_结束考勤")

    """ ------- 学生角色 ------- """

    def go_to_sign_attend(self, attend_number:str):
        """
        立即签到
        :return:
        """

        # 签到弹框_立即签到
        self.click_ele(loc.sign_up_button, "班集页面_签到弹窗_立即签到")
        # 签到弹框_输入考勤码
        self.input_value_for_ele(loc.input_attend, "班集页面_签到弹窗_输入考勤码", attend_number)







