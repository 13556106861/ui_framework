# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

import os
from common.log_handle import LogHandle
from conf.project_path import log_path
from common.config_handle import conf


class ProjectLog(LogHandle):

    """ 仅适用于当前项目的日志输出 """

    log_name = os.path.join(log_path, conf.get_str("log", "name"))

    def __init__(self):
        super().__init__(collect_name=conf.get_str("log", "collector_name"),
                         collect_level=conf.get_str("log", "collector_level"),
                         file_name=self.log_name,
                         fmt=conf.get_str("log", "format"))


logger = ProjectLog()

if __name__ == '__main__':
    logger = ProjectLog()
    logger.info("测试")
    print(logger.log_name)