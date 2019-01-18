# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2019/1/19
Description:
    quick_test_starter.py
----------------------------------------------------------------------------"""

import importlib

TEST_MODULE = "frame_grabber"

if __name__ == '__main__':
    test_module = importlib.import_module("quick_test.%s" % TEST_MODULE)
    test_module.test()
