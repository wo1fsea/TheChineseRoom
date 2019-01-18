# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
	Huang Quanyong
	gzhuangquanyong@corp.netease.com
Date:
	2019/1/18
Description:
	quick_test_starter
----------------------------------------------------------------------------"""

TEST_MODULE = "window_controller"

import importlib

if __name__ == '__main__':
	test_module = importlib.import_module("quick_test.%s" % TEST_MODULE)
	test_module.test()
