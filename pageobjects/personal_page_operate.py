# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

from common.base_page_operate import BasePageOperate
from pagelocators.personal_page_loc import PersonalPageLoc as loc
from pageobjects.index_page_operate import IndexPageOperate


class PersonalPageOperate(BasePageOperate):
    """ 用户个人设置页面各元素操作 """

    def get_user_nickname(self):
        """
        获取用户昵称
        :return: 用户昵称
        """

        nickname = self.get_element_text(loc.user_name, "个人设置页面_获取用户昵称")

        return nickname