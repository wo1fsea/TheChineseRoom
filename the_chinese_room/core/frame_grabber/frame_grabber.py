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
from the_chinese_room.utils.singleton import Singleton


class FrameGrabber(Singleton):
	"""
	frame grabber
	"""

	def __init__(self):
		super(FrameGrabber, self).__init__()
		self._mss = mss.mss()

	def grab(self, regions):
		"""
		grab
		:param regions: list of regions, [utils.rect.Rect(), ...]
		:return: list of PIL images, []
		"""
		monitor = self._mss.monitors[0]

		width = monitor["width"]
		height = monitor["height"]
		left = monitor["left"]
		top = monitor["top"]

		screen_shot = self._mss.grab(monitor)
		screen_shot_img = Image.frombytes('RGB', screen_shot.size, screen_shot.rgb)
		screen_shot_img = screen_shot_img.resize((width, height))
		imgs = [
			screen_shot_img.crop((
				region.left - left,
				region.top - top,
				region.right - left,
				region.bottom - top
			))
			for region in regions
		]
		return imgs
