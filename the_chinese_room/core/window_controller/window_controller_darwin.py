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

APPLE_SCRIPT_LOCATE_WINDOW = """
tell application "System Events" to tell processes
    set names to name
    set wins to (windows whose name is "{title}")
end tell

set pnames to {{}}
repeat with n from 1 to length of names
    if item n of wins is not {{}} then
        copy item n of names to the end of pnames
    end if
end repeat

if length of pnames is not 0 then
    return item 1 of pnames
else
    return ""
end if
"""

APPLE_SCRIPT_FOCUS_WINDOW_NAME = """
tell application "System Events"
    set titles to title of the windows of (first application process whose frontmost is true)
end tell

if length of titles is not 0 then
    return item 1 of titles 
else
    return ""
end if

"""


class WindowControllerDarwin(WindowController):
	"""

	"""

	def __init__(self):
		pass

	def locate_window_by_pid(self, pid):
		return pid

	def locate_window_by_title(self, title):
		# names = applescript.run(APPLE_SCRIPT_LOCATE_WINDOW.format(title=title)).out
		# return names
		return title

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

	def get_window_geometry(self, window_id):
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

	def get_window_inner_geometry(self, window_id):
		raise NotImplementedError()
