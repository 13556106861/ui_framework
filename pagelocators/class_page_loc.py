# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

from selenium.webdriver.common.by import By


class ClassPageLoc:
    """ 课程页面各元素的定位表达式 """

    """ ------- 老师角色 ------- """

    # 考勤控件
    attend_button = (By.XPATH, "//i[@class='iconfont iconkaoqin']/following-sibling::span")

    # iframe
    attend_iframe = (By.XPATH, "//iframe[@id='layui-layer-content1']")

    # 新建考勤
    add_attend = (By.XPATH, "//a[text()='新建考勤']")

    # 数字考勤
    digit_attend = (By.XPATH, "//div[@class='iconarea digit']//div[@class='icons']")

    # 开始考勤
    start_attend = (By.XPATH, '//div[@id="new-perform"]//a[text()="开始考勤"]')

    # 考勤码(共匹配4个span元素，每个span标签的文本是一个考勤码数字)
    attend_number = (By.XPATH, "//div[@class='number-box']//span")

    # 获取签到人数
    signed_up_count = (By.XPATH, "//div[@id='number-attend']//i[@class='ing']")

    # 结束考勤
    end_attend_button = (By.XPATH, "//div[@id='number-attend']//a[text()='结束']")

    # 确认结束考勤
    sure_end_attend_butten = (By.XPATH, "//div[@id='end-attend']//a[@class='sure active']")

    """ ------- 学生角色 ------- """

    # 立即签到
    sign_up_button = (By.XPATH, "//a[text()='立即签到']")

    # 签到弹框 - 考勤码输入框
    input_attend = (By.XPATH, "//input[@class='vc-n-input j_modalAuthInput']")






