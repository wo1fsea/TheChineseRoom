# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2019/1/19
Description:
    auto.py
----------------------------------------------------------------------------"""

from ..core.input_controller.keys import Mouse


class Auto(object):
    """

    """
    def __init__(self):
        pass

    def set_region(self, rect):
        pass

    def key_press(self, key):
        pass

    def key_release(self, key):
        pass

    def key_tap(self, key):
        pass

    def mouse_press(self, button=Mouse.BUTTON_LEFT, position=(None, None)):
        pass

    def mouse_release(self, button=Mouse.BUTTON_LEFT, position=(None, None)):
        pass

    def mouse_click(self, button=Mouse.BUTTON_LEFT, position=(None, None)):
        pass

    def mouse_move_to(self, position):
        pass

    def mouse_scroll(self, amount, position=(None, None)):
        pass
