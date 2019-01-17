# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
	Huang Quanyong
	gzhuangquanyong@corp.netease.com
Date:
	2019/1/17
Description:
	cv_utils
----------------------------------------------------------------------------"""

import cv2
import numpy
from PIL import ImageDraw


def pil_image_2_cv_image(pil_image):
	open_cv_image = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
	return open_cv_image


def pil_image_2_cv_image_gray(pil_image):
	open_cv_image = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2GRAY)
	return open_cv_image


def mark_regions_in_pil_image(pil_image, regions):
	draw = ImageDraw.Draw(pil_image)
	for region in regions:
		draw.rectangle((region["left"], region["top"], region["right"], region["bottom"]), outline="red")
	return pil_image
