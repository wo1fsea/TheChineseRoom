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
    ag.start_host_program(r"F:\SSS\ScreenToGif 2.exe")

    cur_py_path, _ = os.path.split(os.path.abspath(__file__))
    ag.click_on_template(os.path.join(cur_py_path, "record.png"))

    ag.sleep(5)
    ag.kill_host_program()
