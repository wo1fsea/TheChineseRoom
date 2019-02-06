# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2019/2/6
Description:
    agent.py
----------------------------------------------------------------------------"""

from ..core.input_controller.keys import Mouse
from ..core.input_controller import InputController
from ..core.frame_grabber import FrameGrabber
from ..core.window_controller import WindowController
from ..core.process_controller import ProcessController
from ..core.cv.template_matcher import TemplateMatcher

import time
from PIL import Image


class Agent(object):
    """

    """

    CHECK_INTERVAL = 0.1

    def __init__(self):
        self.host_window_id = None
        self.host_pid = None
        self.region = None

        self.wc = WindowController()
        self.pc = ProcessController()
        self.fg = FrameGrabber()
        self.ic = InputController()
        self.tm = TemplateMatcher()

    def _focus_host_window(self):
        assert self.host_window_id, "has no host window"
        self.wc.focus_window(self.host_window_id)

    def _refresh_region(self):
        assert self.host_window_id, "has no host window"
        self.region = self.wc.get_window_geometry(self.host_window_id)

    def start_host_program(self, path):
        assert self.host_window_id is None, "already has a host window"
        p = self.pc.start_progress(path)
        self.host_pid = p.pid
        self.host_window_id = self.wc.locate_window_by_pid(p.pid)

    def kill_host_program(self):
        self.pc.kill(self.host_pid)

    def set_region(self, rect):
        self.region = rect
        self.wc.move_window(self.host_window_id, rect.x, rect.y)
        self.wc.resize_window(self.host_window_id, rect.width, rect.height)

    def key_press(self, key):
        self._focus_host_window()
        self.ic.key_press(key)

    def key_release(self, key):
        self._focus_host_window()
        self.ic.key_release(key)

    def key_tap(self, key):
        self._focus_host_window()
        self.ic.key_tap(key)

    def type_text(self, text):
        raise NotImplementedError()

    def mouse_press(self, button=Mouse.BUTTON_LEFT, position=(None, None)):
        self._focus_host_window()
        self._refresh_region()
        if position != (None, None):
            position = (position[0] + self.region.left, position[1] + self.region.top)
        self.ic.mouse_press(button, position)

    def mouse_release(self, button=Mouse.BUTTON_LEFT, position=(None, None)):
        self._focus_host_window()
        self._refresh_region()
        if position != (None, None):
            position = (position[0] + self.region.left, position[1] + self.region.top)
        self.ic.mouse_release(button, position)

    def mouse_click(self, button=Mouse.BUTTON_LEFT, position=(None, None)):
        self._focus_host_window()
        self._refresh_region()
        if position != (None, None):
            position = (position[0] + self.region.left, position[1] + self.region.top)
        self.ic.mouse_click(button, position)

    def mouse_move_to(self, position):
        self._focus_host_window()
        self._refresh_region()
        if position != (None, None):
            position = (position[0] + self.region.left, position[1] + self.region.top)
        self.ic.mouse_move_to(position)

    def mouse_scroll(self, amount, position=(None, None)):
        self._focus_host_window()
        self._refresh_region()
        if position != (None, None):
            position = (position[0] + self.region.left, position[1] + self.region.top)
        self.ic.mouse_scroll(amount, position)

    def grab_frame(self):
        self._focus_host_window()
        self._refresh_region()
        frames = self.fg.grab((self.region,))
        return frames[0]

    def _load_image(self, image):
        if isinstance(image, str):
            image = Image.open(image)
        return image

    def find_template(self, template_image):
        template_image = self._load_image(template_image)

        frame = self.grab_frame()
        regions = self.tm.find_all(frame, template_image)
        return regions

    def click_on_template(self, template_image, button=Mouse.BUTTON_LEFT, center_offset=(0, 0), timeout=0):
        template_image = self._load_image(template_image)

        start_time = time.time()

        while True:
            regions = self.find_template(template_image)
            if regions:
                region = regions[0]
                position = region.center
                position = (position[0] + center_offset[0], position[1] + center_offset[1])
                self.mouse_click(button, position)
                return True

            if time.time() - start_time > timeout:
                break

            self.sleep(self.CHECK_INTERVAL)

        return False

    def sleep(self, second):
        time.sleep(second)

    def check_pixel(self, position, color, timeout=0):
        pass

    def check_template(self, template_image, region=None, timeout=0):
        template_image = self._load_image(template_image)
        if region is None:
            region = self.region

        start_time = time.time()

        while True:
            regions = self.find_template(template_image)
            for r in regions:
                if r in region:
                    return True

            if time.time() - start_time > timeout:
                break

            self.sleep(self.CHECK_INTERVAL)

        return False
