# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2019/1/15
Description:
    frame_grabber.py
----------------------------------------------------------------------------"""

import mss
from PIL import Image


class FrameGrabber(object):
    def __init__(self):
        super(FrameGrabber, self).__init__()
        self._mss = mss.mss()

    def grab(self, regions):
        """
        grab
        :param regions: list of regions, [{"left": int, "top": int, "width": int, "height": int}, ...]
        :return: list of PIL images, []
        """
        monitor = self._mss.monitors[0]

        left = monitor["left"]
        top = monitor["top"]
        width = monitor["width"]
        height = monitor["height"]

        screen_shot = self._mss.grab(monitor)
        screen_shot_img = Image.frombytes('RGB', screen_shot.size, screen_shot.rgb)
        screen_shot_img = screen_shot_img.resize((width, height))
        imgs = [
            screen_shot_img.crop((
                region["left"] - left,
                region["top"] - top,
                region["width"] + region["left"] - left,
                region["height"] + region["top"] - top
            ))
            for region in regions
        ]
        return imgs


if __name__ == '__main__':
    fg = FrameGrabber()
    imgs = fg.grab(
        [
            {"left": -100, "top": 0, "width": 100, "height": 100},
            {"left": 0, "top": 0, "width": 100, "height": 100}
        ]
    )
    for img in imgs:
        img.show()
