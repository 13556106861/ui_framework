# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

import os
import logging
from datetime import datetime


def check_file_name(file_name):
    """ 校验文件名是否包含目录路径，包含则返回目录与文件名（不包含目录），不包含则返回False """

    if os.path.isabs(file_name):
        if os.path.exists(os.path.dirname(file_name)):
            dir_name = os.path.dirname(file_name)
            f_name = os.path.basename(file_name)
            return dir_name, f_name
        else:
            raise FileNotFoundError("{} path is not found".format(file_name))
    else:
        return False


class LogHandle(logging.Logger):
    now_time = datetime.now().strftime("%Y-%m-%d")

    def __init__(self,
                 collect_name,
                 collect_level='DEBUG',
                 handle_level=None,
                 file_name=None,
                 fmt=None):
        """

        :param collect_name: 收集器名称
        :param collect_level: 收集器等级
        :param handle_level: 处理器等级
        :param file_name: 日志文件名/包含路径的日志文件名
        :param fmt: 日志输出格式
        """
        # 调用父类Logger的初始化方法创建一个日志收集器实例并设置日志收集器级别
        super().__init__(collect_name, collect_level)

        # 创建日志处理器（file_name为空则创建控制台处理器，否则创建文件处理器）
        if file_name is None:
            # 创建控制台处理器实例
            handler = logging.StreamHandler()
        else:
            # 创建文件处理器实例（无论文件名是否包含路径均与类属性获取到的日期相拼接组成包含当前日期的文件名）
            try:
                result = check_file_name(file_name)
            except Exception as e:
                raise e
            else:
                if result:
                    # log日志名与时间拼接
                    f_name = f"{self.now_time}-{result[1]}"
                    # 拼接完整的Log文件路径
                    new_file = os.path.join(result[0], f_name)
                else:
                    new_file = f"{self.now_time}-{file_name}"

            handler = logging.FileHandler(new_file, encoding="utf-8")

        # 设置日志处理器级别（若不传递参数则不设置，不设置则会将收集器收集到的所有日志进行处理输出）
        if handle_level is not None:
            handler.setLevel(handle_level)

        # 设置日志处理器输出格式（若不传递格式则使用默认格式）
        if fmt is not None:
            formatter = logging.Formatter(fmt)
        else:
            fmt_info = '[%(asctime)s %(name)s %(levelname)s %(filename)s lineno:%(lineno)s]: %(message)s'
            formatter = logging.Formatter(fmt_info)
        # 设置日志处理器输出格式
        handler.setFormatter(formatter)

        # 日志收集器关联日志处理器(Logger类的实例就是一个日志收集器，可用self调用Logger类的addHandler方法来关联日志处理器)
        self.addHandler(handler)







