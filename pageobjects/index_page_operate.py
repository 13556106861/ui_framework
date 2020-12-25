# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe
from selenium.webdriver.common.by import By
from common.base_page_operate import BasePageOperate
from pagelocators.index_page_loc import IndexPageLoc as loc


class IndexPageOperate(BasePageOperate):
    """ 课堂首页各元素的操作 """

    def click_course(self, course_name):
        """
        课堂首页点击名称为course_name的课程
        :param course_name:  课程名称
        :return: None
        """

        # 替换元素表达式的值
        new_loc = self.update_loc_value(loc.class_name_link, course_name)
        # 点击课程
        self.click_ele(new_loc, f"课程首页_点击{course_name}课程")

    def click_head_img(self):
        """
        点击用户头像
        :return: None
        """

        self.click_ele(loc.user_head, "课程首页_点击用户头像")

    def click_personal_set(self):
        """
        头像下拉项_点击个人设置
        :return: None
        """

        self.click_ele(loc.set_up, "课程首页_用户头像下拉项_点击个人设置")

    @staticmethod
    def update_loc_value(loc:tuple, new_value):
        """
        使用new_value替换掉loc当中的元素表达式
        :param loc: 元组类型的元素定位表达式
        :param new_value: 要替换到元素定位表达式的值
        :return: 替换之后的元素表达式（元组类型）
        """

        new_expr = loc[1].format(new_value)

        return loc[0], new_expr


if __name__ == '__main__':

    def update_loc_value(expr:str, new_value):
        """
        使用new_value替换掉expr当中的值
        :param loc: str类型
        :param new_value: 要替换到元素定位表达式的值
        :return: 替换之后的数据（str)
        """

        new_expr = expr.format(new_value)

        return new_expr

    course_name = "'Renee Brooks'"
    class_name_link = (eval('By.XPATH'), "//a[text()={}]")
    a = update_loc_value(class_name_link[1], course_name)
    new_name = (By.XPATH, a)
    print(a)





