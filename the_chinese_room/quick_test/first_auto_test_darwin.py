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

from the_chinese_room.core.cv.template_matcher import TemplateMatcher
from the_chinese_room.core.window_controller import WindowController
from the_chinese_room.core.input_controller import InputController
from the_chinese_room.core.frame_grabber import FrameGrabber

from PIL import Image
import time


def test():
    tm = TemplateMatcher()
    wc = WindowController()
    ic = InputController()
    fg = FrameGrabber()

    p_name = "Calculator"
    print(wc.locate_window(p_name))
    wc.focus_window(p_name)
    temp8 = Image.open("8.png")
    temp6 = Image.open("6.png")

    win_rect = wc.get_window_geometry(p_name)
    frame = fg.grab([win_rect])[0]
    # frame.show()
    rect8 = tm.find_the_best(frame, temp8)
    rect6 = tm.find_the_best(frame, temp6)

    time.sleep(0.5)

    ic.mouse_click(position=(win_rect.x + rect8.x + rect8.width / 2, win_rect.y + rect8.y + rect8.height / 2))
    time.sleep(0.5)
    ic.mouse_click(position=(win_rect.x + rect8.x + rect8.width / 2, win_rect.y + rect8.y + rect8.height / 2))
    time.sleep(0.5)
    ic.mouse_click(position=(win_rect.x + rect6.x + rect6.width / 2, win_rect.y + rect6.y + rect8.height / 2))
