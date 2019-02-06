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
import psutil

from the_chinese_room.utils.rect import Rect

from .window_controller import WindowController

APPLE_SCRIPT_LOCATE_WINDOW = """
tell application "System Events" to tell process "{title}"
    return id 
end tell

"""

APPLE_SCRIPT_LOCATE_WINDOW_BY_TITLE = """
tell application "System Events" to tell processes
    return {{name, windows whose name is "{title}"}}
end tell
"""


class WindowControllerDarwin(WindowController):
    def __init__(self):
        pass

    def locate_window_by_pid(self, pid):
        names = []
        for p in psutil.process_iter():
            if p.pid == pid:
                names.append(p.name())
        return names[0] if names else ""

    def locate_window_by_title(self, title):
        names, windows = applescript.AppleScript(APPLE_SCRIPT_LOCATE_WINDOW_BY_TITLE.format(title=title)).run()
        names = map(lambda x: x[0], filter(lambda x: x[1], zip(names, windows)))
        return names[0] if names else ""

    def move_window(self, p_name, x, y):
        applescript.AppleScript('''
            tell application "System Events" to tell window 1 of process "{p_name}"
                set position to {{ {x}, {y} }}
            end tell
        '''.format(p_name=p_name, x=x, y=y)).run()

    def resize_window(self, p_name, width, height):
        applescript.AppleScript('''
            tell application "System Events" to tell window 1 of process "{p_name}"
                set size to {{ {width}, {height} }}
            end tell
        '''.format(p_name=p_name, width=width, height=height)).run()

    def focus_window(self, p_name):
        applescript.AppleScript('''
            tell application "System Events" to tell process "{p_name}"
                set frontmost to true
            end tell
        '''.format(p_name=p_name)).run()

    def is_window_focused(self, p_name):
        return self.get_focused_window_name() == p_name

    def get_focused_window_name(self):
        p_name = applescript.AppleScript('''
            tell application "System Events"
                return title of first application process whose frontmost is true
            end tell
        ''').run()
        return p_name

    def get_window_geometry(self, p_name):
        window_geometry = applescript.AppleScript('''
            tell application "System Events" to tell process "{p_name}"
                return get size of window 1
            end tell
        '''.format(p_name=p_name)).run()

        width, height = window_geometry

        window_information = applescript.AppleScript('''
            tell application "System Events" to tell window 1 of process "{p_name}"
                return get position
            end tell
        '''.format(p_name=p_name)).run()

        x, y = window_information

        return Rect(x, y, width, height)

    def get_window_inner_geometry(self, p_name):
        return self.get_window_geometry(p_name)
