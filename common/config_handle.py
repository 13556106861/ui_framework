# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

from configparser import ConfigParser
from conf.project_path import conf_path
import os


class ConfigHandle(ConfigParser):

    def __init__(self, conf_file_name, encoding="utf-8"):
        """

        :param conf_file_name: 配置文件名称
        """
        self.file_name = conf_file_name
        self.encoding = encoding

        # 调用父类的初始化方法为实例初始化（初始化后才能用到初始化方法中的实例属性，读取配置文件用到了初始化方法的属性，必须初始化操作）
        super().__init__()   # 也可使用第二种方案，不继承直接在此处实例化ConfigParser类对象

        # 加载（读取）配置文件到内存中（后续对配置文件的进一步操作都是针对内存中的配置文件数据来操作的）
        self.read(self.file_name, self.encoding)

    def get_str(self, section, option):
        """
        读取数据（读取出来的数据将是str类型）
        :param section: 配置块
        :param option: 配置项
        :return: 对应配置项的数据
        """

        return self.get(section, option)

    def get_int(self, section, option):
        """
        读取数据（读取出来的数据将是int类型）
        :param section: 配置块
        :param option: 配置项
        :return: 对应配置项的数据
        """

        return self.getint(section, option)

    def get_float(self, section, option):
        """
        读取数据（读取出来的数据将是float类型）
        :param section: 配置块
        :param option: 配置项
        :return: 对应配置项的数据
        """

        return self.getfloat(section, option)

    def get_bool(self, section, option):
        """
        读取数据（读取出来的数据将是bool类型）
        :param section: 配置块
        :param option: 配置项
        :return: 对应配置项的数据
        """

        return self.getboolean(section, option)

    def get_section_values(self, section):
        """ 获取指定section下所有option的值 """

        try:
            return dict(self.items(section))
        except Exception:
            raise

    def write_data(self, section, option, value):
        """
        向指定配置块中写入数据
        :param section: 配置块
        :param option: 配置项
        :param value: 对应配置项的数据
        :return: None
        """

        # 写入内容
        self.set(section, option, value)
        # 保存到配置文件
        self.write(open(self.file_name, "w", encoding=self.encoding))


conf = ConfigHandle(os.path.join(conf_path, "conf.ini"))

if __name__ == '__main__':
    conf = ConfigHandle(os.path.join(conf_path, "conf.ini"))

    print(dict(conf.items("admin")))

