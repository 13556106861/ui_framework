# -*- coding:utf-8 -*-
# Email:84351228@qq.com
# Author:KeKe

import pytest


if __name__ == "__main__":
    pytest.main(["--alluredir=outputs/reports",
                 "-m smoke and regression"])
