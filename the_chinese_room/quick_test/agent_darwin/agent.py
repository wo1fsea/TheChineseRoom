# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2019/1/20
Description:
    first_auto_test_darwin.py
----------------------------------------------------------------------------"""

import os
from the_chinese_room.agent import Agent


def test():
    ag = Agent()
    ag.start_host_program("/Applications/Calculator.app/Contents/MacOS/Calculator")

    cur_py_path, _ = os.path.split(os.path.abspath(__file__))
    ag.click_on_template(os.path.join(cur_py_path, "8.png"))
    ag.click_on_template(os.path.join(cur_py_path, "8.png"))
    ag.click_on_template(os.path.join(cur_py_path, "6.png"))

    ag.sleep(5)
    ag.kill_host_program()
