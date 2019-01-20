# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/10/4
Description:
    window_controller_win32.py
----------------------------------------------------------------------------"""

import win32gui

from the_chinese_room.utils.rect import Rect
from .window_controller import WindowController


class WindowControllerWin32(WindowController):
    def __init__(self):
        pass

    def locate_window(self, title):
        return win32gui.FindWindow(None, title)

    def move_window(self, window_id, x, y):
        x0, y0, x1, y1 = win32gui.GetWindowRect(window_id)
        win32gui.MoveWindow(window_id, x, y, x1 - x0, y1 - y0, True)

    def resize_window(self, window_id, width, height):
        x0, y0, x1, y1 = win32gui.GetWindowRect(window_id)
        win32gui.MoveWindow(window_id, x0, y0, width, height, True)

    def focus_window(self, window_id):
        win32gui.SetForegroundWindow(window_id)

    def is_window_focused(self, window_id):
        focused_window_id = win32gui.GetForegroundWindow()
        return focused_window_id == window_id

    def get_focused_window_name(self):
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())

    def get_window_geometry(self, window_id):
        x, y, width, height = win32gui.GetClientRect(window_id)
        rect = Rect(x, y, width, height)

        return rect

    def get_window_inner_geometry(self, window_id):
        x, y, width, height = win32gui.GetClientRect(window_id)
        x0, y0, x1, y1 = win32gui.GetWindowRect(window_id)

        border_width = ((x1 - x0 - width) // 2)

        x = x0 + border_width
        y = y0 + (y1 - y0 - height - border_width)

        rect = Rect(x, y, width, height)

        return rect
