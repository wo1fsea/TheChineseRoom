# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
	Huang Quanyong
	gzhuangquanyong@corp.netease.com
Date:
	2019/1/18
Description:
	window_controller
----------------------------------------------------------------------------"""

from the_chinese_room.core import window_controller
from the_chinese_room.core import frame_grabber
import time


def test():
	fg = frame_grabber.FrameGrabber()

	wc = window_controller.WindowController()
	w_name = wc.get_focused_window_name()
	w_id = wc.locate_window(w_name)
	w_geometry = wc.get_window_inner_geometry(w_id)
	print("window_name", w_name)
	print("window_id", w_id)
	print("window_geometry", w_geometry)

	wc.resize_window(w_id, 300, 300)
	print("resize")
	time.sleep(1)

	w_geometry = wc.get_window_inner_geometry(w_id)
	print("window_geometry", w_geometry)

	fg.grab([
		{
			"left": w_geometry["x"],
			"top": w_geometry["y"],
			"width": 10,
			"height": 10,
		}
	])[0].show()

	wc.move_window(w_id, 10, 10)
	time.sleep(1)

	w_geometry = wc.get_window_inner_geometry(w_id)
	print("window_geometry", w_geometry)
