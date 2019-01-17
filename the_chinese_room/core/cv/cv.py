# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
	Huang Quanyong
	gzhuangquanyong@corp.netease.com
Date:
	2019/1/17
Description:
	cv
----------------------------------------------------------------------------"""

import cv2
import numpy

import cv_utils

TEMPLATE_MATCH_THRESHOLD = 0.75
HISTOGRAM_TEST_THRESHOLD = 1.
HISTOGRAM_TEST_HIST_SIZE = [4, 4, 4]
HISTOGRAM_TEST_RANGE = [0, 256, 0, 256, 0, 256]


class TemplateMatcher(object):
	def __init__(
			self,
			threshold=TEMPLATE_MATCH_THRESHOLD,
			histogram_test=False,
			histogram_test_threshold=HISTOGRAM_TEST_THRESHOLD
	):
		self._threshold = threshold
		self._histogram_test = histogram_test
		self._histogram_test_threshold = histogram_test_threshold

	def _calc_hist(self, image):
		return cv2.normalize(
			cv2.calcHist(
				[image],
				[0, 1, 2],
				None,
				HISTOGRAM_TEST_HIST_SIZE,
				HISTOGRAM_TEST_RANGE
			),
			None,
			norm_type=cv2.NORM_L1
		)

	def _diff_hist(self, hist0, hist1):
		print(abs(hist0 - hist1).sum())
		return abs(hist0 - hist1).sum()

	def _histogram_test_filter(self, image, template, regions):
		if not regions:
			return regions

		template_hist = self._calc_hist(template)

		filtered_regions = []
		for region in regions:
			hist = self._calc_hist(
				image[region["top"]:region["bottom"] + 1, region["left"]:region["right"] + 1, :]
			)

			if self._diff_hist(template_hist, hist) < self._histogram_test_threshold:
				filtered_regions.append(regions)

		return regions

	def find_all(self, image, template):
		""""
		find all matched region
		:param image:
		:param template:
		:return: regions, [{"left": int, "top": int, "width": int, "height": int}, ...]
		"""
		regions = []
		image = cv_utils.pil_image_2_cv_image(image)
		template = cv_utils.pil_image_2_cv_image(template)
		image_gray = cv_utils.pil_image_2_cv_image_gray(image)
		template_gray = cv_utils.pil_image_2_cv_image_gray(template)

		height, width = template_gray.shape
		result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)

		loc = numpy.where(result >= self._threshold)
		for pos in zip(*loc[::-1]):
			x, y = pos
			regions.append(
				{
					"left": x,
					"top": y,
					"right": x + width - 1,
					"bottom": y + height - 1,
					"match_value": result[y][x]
				}
			)

		regions.sort(key=lambda x: x["match_value"], reverse=True)
		print(regions)

		if self._histogram_test:
			regions = list(self._histogram_test_filter(image, template, regions))

		return regions

	def find_the_best(self, image, template):
		regions = self.find_all(image, template)
		return regions[0] if regions else None


if __name__ == '__main__':
	from PIL import Image

	tm = TemplateMatcher(histogram_test=False)
	img = Image.open("d:/test.png")
	temp = Image.open("d:/temp.png")
	regions = tm.find_all(img, temp)
	print(regions)
	cv_utils.mark_regions_in_pil_image(img, regions)
	img.show()
