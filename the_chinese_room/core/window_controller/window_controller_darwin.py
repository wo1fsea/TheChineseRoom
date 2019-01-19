# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/10/5
Description:
    window_controller_darwin.py
----------------------------------------------------------------------------"""

import applescript

from the_chinese_room.utils.rect import Rect

from .window_controller import WindowController


class WindowControllerDarwin(WindowController):
    def __init__(self):
        pass

    def locate_window(self, name):
        return name

    def move_window(self, window_id, x, y):
        applescript.run('''
            tell application "System Events" to tell window 1 of process "{window_id}"
                set position to {{ {x}, {y} }}
            end tell
        '''.format(window_id=window_id, x=x, y=y))

    def resize_window(self, window_id, width, height):
        applescript.run('''
            tell application "System Events" to tell window 1 of process "{window_id}"
                set size to {{ {width}, {height} }}
            end tell
        '''.format(window_id=window_id, width=width, height=height))

    def focus_window(self, window_id):
        applescript.run('''
            tell application "System Events" to tell process "{window_id}"
                set frontmost to true
            end tell
        '''.format(window_id=window_id))

    def is_window_focused(self, window_id):
        return self.get_focused_window_name() == window_id

    def get_focused_window_name(self):
        focused_window_id = applescript.run('''
            tell application "System Events"
                return title of first application process whose frontmost is true
            end tell
        ''').out

        return focused_window_id

    def get_window_inner_geometry(self, window_id):
        window_geometry = applescript.run('''
            tell application "System Events" to tell process "{window_id}"
                return get size of window 1
            end tell
        '''.format(window_id=window_id)).out

        width, height = map(int, window_geometry.split(","))

        window_information = applescript.run('''
            tell application "System Events" to tell window 1 of process "{window_id}"
                return get position
            end tell
        '''.format(window_id=window_id)).out

        x, y = map(int, window_information.split(","))

        return Rect(x, y, width, height)
