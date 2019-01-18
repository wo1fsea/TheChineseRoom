# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2019/1/19
Description:
    frame_grabber.py
----------------------------------------------------------------------------"""

from the_chinese_room.core.frame_grabber import FrameGrabber
from the_chinese_room.utils.rect import Rect


def test():
    fg = FrameGrabber()
    imgs = fg.grab(
        [
            Rect(100, 100, 100, 100),
            Rect(100, 100, 10, 10),
        ]
    )

    for img in imgs:
        img.show()
