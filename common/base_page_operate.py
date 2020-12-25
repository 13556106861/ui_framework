# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

import os
from time import sleep
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from middle_ware.project_log import logger
from conf.project_path import screenshots_path


class BasePageOperate:
    """ 对元素操作的一系列通用方法 """

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def _wait_ele_visible(self, loc, img_desc:str, time_out=20, poll_time=0.5):
        """
        等待元素可见
        :param loc: 元素定位表达式
        :param img_desc: 图片描述信息，包含页面名称与事件名称，如 登录页面_点击登录控件
        :param time_out: 等待上限
        :param poll_time: 轮询时间
        :return: None
        """
        logger.info(f"{img_desc}:等待{loc}元素可见")

        try:
            # 等待元素可见前获取系统当前时间
            start_time = datetime.now()
            WebDriverWait(self.driver, time_out, poll_frequency=poll_time).until(EC.visibility_of_element_located(loc))
        except:
            # 元素等待过程中抛出异常时则记录日志并截取元素所在的页面图片并保存
            logger.exception(f"{img_desc}: 等待{loc}元素可见失败，错误信息：")
            self.save_page_screenshot(img_desc)
            raise
        else:
            # 等待元素可见成功后再次获取当前系统时间
            end_time = datetime.now()
            logger.info(f"等待{loc}元素可见成功，等待开始时间：{start_time}, "
                        f"等待结束时间：{end_time}, 等待耗时：{end_time - start_time}")

    def _wait_ele_exist(self, loc, img_desc:str, time_out=20, poll_time=0.5):
        """
        等待元素存在
        :param loc: 元素定位表达式
        :param img_desc: 图片描述信息，包含页面名称与事件名称，如 登录页面_点击登录控件
        :param time_out: 等待上限
        :param poll_time: 轮询时间
        :return: None
        """

        logger.info(f"{img_desc}: 等待{loc}元素存在")

        try:
            # 等待元素存在前获取当前系统时间
            start_time = datetime.now()
            WebDriverWait(self.driver, time_out, poll_time).until(EC.presence_of_element_located(loc))
        except:
            # 元素等待过程中抛出异常时则记录日志并截取保存元素所在的页面
            logger.exception(f"{img_desc}：等待{loc}元素存在失败，错误信息:")
            self.save_page_screenshot(img_desc)
            raise
        else:
            # 元素可见后再次获取当前系统时间
            end_time = datetime.now()
            logger.info(f"等待{loc}元素存在成功，开始时间为{start_time}，"
                        f"结束时间为{end_time},等待耗时：{end_time - start_time}")

    def _get_element(self, loc, img_desc:str):
        """
        查找元素
        :param loc: 元素定位表达式
        :param img_desc: 图片描述信息，包含页面名称与事件名称，如 登录页面_点击登录控件
        :return: None
        """

        logger.info(f"{img_desc}: 查找{loc}元素")

        try:
            ele = self.driver.find_element(*loc)
            return ele
        except:
            logger.exception(f"查找{loc}元素失败，错误信息：")
            self.save_page_screenshot(img_desc)
            raise

    def get_elements(self, loc, img_doc, time_out=20, poll_time=0.5):
        """
        查找多个元素
        :param loc: 元素定位表达式
        :param img_doc: 图片描述信息，包含页面名称与事件名称，如 登录页面_点击登录控件
        :param time_out: 等待上限
        :param poll_time: 等待轮询时间
        :return: None
        """

        logger.info(f"查找{loc}元素")

        # 等待元素可见
        self._wait_ele_visible(loc, img_doc, time_out, poll_time)
        sleep(1)

        try:
            eles = self.driver.find_elements(*loc)
            return eles
        except:
            logger.exception(f"查找{loc}元素失败，错误信息：")
            raise

    def click_ele(self, loc, img_desc:str, time_out=30, poll_time=0.5, scroll_flag=False):
        """ click:点击元素 """

        # 等待元素可见并定位元素
        self._wait_ele_visible(loc, img_desc, time_out, poll_time)
        ele = self._get_element(loc, img_desc)

        # 将元素滚动到可视区内
        if scroll_flag:
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)

        logger.info(f"{img_desc}：点击{loc}元素")

        try:
            sleep(3)
            ele.click()
        except:
            logger.exception(f"点击{loc}元素失败，错误信息：")
            # 截图并保存
            self.save_page_screenshot(img_desc)
            raise

    def input_value_for_ele(self, loc, img_desc:str, value, time_out=20, poll_time=0.5, scroll_flag=False):
        """
        输入数据
        :param loc: 元素定位表达式
        :param img_desc: 图片描述信息，包含页面名称与事件名称，如 登录页面_点击登录控件
        :param value: 要输入的数据
        :param time_out: 等待上限
        :param poll_time: 等待轮询时间
        :param scroll_flag: 滚动条开关，True：需要将元素滚动到可视区，False：不需要将元素滚动到可视区
        :return: None
        """

        # 等待元素可见
        self._wait_ele_visible(loc, img_desc, time_out, poll_time)
        # 查找元素
        ele = self._get_element(loc, img_desc)
        # 将元素滚动到可视区内
        if scroll_flag:
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)

        logger.info(f"{img_desc}：向{loc}元素输入文本：{value}")
        try:
            ele.send_keys(value)
            logger.info(f"{loc}元素成功输入'{value}'文本")
        except:
            logger.exception(f"{loc}元素输入'{value}'文本失败，错误信息：")
            # 截图保存
            self.save_page_screenshot(img_desc)
            raise

    def get_element_text(self, loc, img_desc:str, time_out=20, poll_time=0.5, scroll_flag=False):
        """
        获取元素的文本
        :param loc: 元素定位表达式 或 WebElement对象
        :param img_desc: 图片描述信息，包含页面名称与事件名称，如 登录页面_点击登录控件
        :param time_out: 等待上限
        :param poll_time: 等待轮询时间
        :param scroll_flag: 滚动条开关，True：需要将元素滚动到可视区，False：不需要将元素滚动到可视区
        :return: None
        """
        if isinstance(loc, tuple):
            # 等待元素可见
            self._wait_ele_visible(loc, img_desc, time_out, poll_time)
            # 查找元素
            ele = self._get_element(loc, img_desc)
        else:
            ele = loc

        # 将元素滚动到可视区内
        if scroll_flag:
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)

        logger.info(f"{img_desc}：获取{loc}元素的文本")

        try:
            text = ele.text
            logger.info(f"成功获取{loc}元素的文本：{text}")
        except:
            logger.exception(f"获取{loc}元素的文本失败，错误信息:")
            self.save_page_screenshot(img_desc)
            raise
        else:
            return text

    def get_attribute_value(self, loc, attr_name, img_desc:str, time_out=30, poll_time=0.5, scroll_flag=False):
        """
        获取元素的xxx属性值
        :param loc: 元素定位表达式
        :param attr_name: 元素属性名
        :param img_desc: 图片描述信息，包含页面名称与事件名称，如 登录页面_点击登录控件
        :param time_out: 等待上限
        :param poll_time: 等待轮询时间
        :param scroll_flag: 滚动条开关，True：需要将元素滚动到可视区，False：不需要将元素滚动到可视区
        :return: None
        """

        # 等待元素存在并定位元素（获取元素属性值只需要元素存在即可不需要可见）
        self._wait_ele_exist(loc, img_desc, time_out, poll_time)
        ele = self._get_element(loc, img_desc)

        # 将元素滚动到可视区内
        if scroll_flag:
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)

        logger.info(f"{img_desc}：获取{loc}元素的{attr_name}属性值")

        try:
            value = ele.get_attribute(attr_name)
            logger.info(f"成功获取{loc}元素的{attr_name}属性值：{value}")
        except:
            logger.exception(f"获取{loc}元素的{attr_name}属性值失败，错误信息:")
            self.save_page_screenshot(img_desc)
            raise
        else:
            return value

    def switch_new_window(self, img_depict):
        """
        切换到新窗口
        :param img_depict:  图片描述信息，包含页面名称与事件名称，如 登录页面_点击登录控件
        :return: None
        """

        # 获取所有窗口句柄（返回列表类型）
        window_handles = self.driver.window_handles

        try:
            # 切换到最新打开的窗口
            self.driver.switch_to.window(window_handles[-1])
            logger.info(f"{img_depict}成功")
        except:
            logger.exception(f"{img_depict}失败，错误信息：")
            self.save_page_screenshot(img_depict)
            raise

    def switch_to_iframe(self, loc, img_desc:str, time_out=20, poll_time=0.5):
        """
        切换到iframe
        :param loc: 元素定位表达式
        :param time_out: 等待上限
        :param poll_time: 等待轮询时间
        :return: None
        """
        logger.info(f"等待并切换到{loc} iframe框架")

        try:
            WebDriverWait(self.driver, time_out, poll_time).until(EC.frame_to_be_available_and_switch_to_it(loc))
            logger.info(f"成功切换进入到{loc} iframe框架")
        except:
            logger.exception(f"切换到{loc}iframe框架失败，错误信息：")
            self.save_page_screenshot(img_desc)
            raise

    def iframe_switch_to_main_document(self):
        """
        从iframe切换到主文档
        :return: None
        """
        try:
            self.driver.switch_to.default_content()
            logger.info(f"从iframe切换到主文档成功")
        except:
            logger.exception(f"从iframe切换到主文档失败，错误信息：")
            raise

    def handle_alert(self, operation, text=None, value=None):
        """
        关闭alert弹窗、获取alert弹窗文本
        :param operation: 操作名，包含（dismiss：否->关闭弹窗, accept：是->关闭弹窗）
        :param text: 参数不为空时表示要获取弹窗文本
        :param value: 表示需要向alert弹窗输入文本
        :return:
        """

        # 获取alert弹框对象
        alert = self.driver.switch_to.alert()

        sleep(1)

        # value不为空则需要向弹窗中输入value
        if value:
            alert.send_keys(value)

        if text:
            value = alert.text
            eval(f"alert.{operation}()")
            return value

        # text为空时则会在text分支直接执行操作关关闭，若text为空则会执行下面的语句
        eval(f"alert.{operation}()")

    def save_page_screenshot(self, img_desc:str):
        """
        对页面进行截图并将截图文件按页面进行分类保存到不同的文件夹
        :param img_desc: 截图命名描述：页面名称_事件名称
        :return: None
        """

        # 获取页面名称
        page_name = img_desc.split("_")[0]

        # 创建截图文件要保存到的文件夹路径
        page_dir = os.path.join(screenshots_path, page_name)
        # 判断文件夹是否存在，不存在则创建
        if not os.path.exists(page_dir):
            os.mkdir(page_dir)

        # 获取系统当前时间并转换成特定格式
        now_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        # 页面截图完整路径：保存截图的文件路径 + 图片描述（页面名称 + 事件名称） + 当前系统时间
        file_name = f"{img_desc}_{now_time}.png"
        save_path = os.path.join(page_dir, file_name)

        # 截图并保存
        try:
            self.driver.save_screenshot(save_path)
            logger.info(f"成功截取{page_name}页面，图片文件保存在：{save_path}")
        except:
            logger.exception(f"{page_name}页面截图保存失败，错误信息：")





