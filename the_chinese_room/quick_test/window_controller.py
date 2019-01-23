# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2019/1/18
Description:
    window_controller.py
----------------------------------------------------------------------------"""

from the_chinese_room.core import window_controller
from the_chinese_room.core import frame_grabber
from the_chinese_room.core import process_controller
import time
import subprocess


def test():
    pc = process_controller.ProcessController()

    print(pc.list_process_names())
    return

    fg = frame_grabber.FrameGrabber()
    p = subprocess.Popen("C:/Program Files/Sublime Text 3/sublime_text.exe")
    wc = window_controller.WindowController()
    w_name = wc.get_focused_window_name()
    time.sleep(1)
    w_id = wc.locate_window_by_pid(p.pid)
    print(w_id)
    w_geometry = wc.get_window_geometry(w_id)
    print("window_name", w_name)
    print("window_id", w_id)
    print("window_geometry", w_geometry.x, w_geometry.y)

    wc.resize_window(w_id, 300, 300)
    print("resize")
    time.sleep(1)

    w_geometry = wc.get_window_geometry(w_id)
    print("window_geometry", w_geometry.x, w_geometry.y)

    fg.grab([
        w_geometry
    ])[0].show()

    wc.move_window(w_id, 10, 10)
    time.sleep(1)

    w_geometry = wc.get_window_geometry(w_id)
    print("window_geometry", w_geometry.x, w_geometry.y)
