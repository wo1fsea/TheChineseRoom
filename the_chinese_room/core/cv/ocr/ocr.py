# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
	Huang Quanyong
	gzhuangquanyong@corp.netease.com
Date:
	2019/1/21
Description:
	ocr
----------------------------------------------------------------------------"""

BACKEND_TESSEROCR = "tesserocr"
DEFAUKT_BACKEND = BACKEND_TESSEROCR


class OCR(object):
	def __init__(self, implement=DEFAUKT_BACKEND):
		super(OCR, self).__init__()
		self._adapter = self._load_adapter(implement)

	def image_to_string(self, pil_image):
		return self._adapter.image_to_string(pil_image)

	def _load_adapter(self, implement):
		if implement == BACKEND_TESSEROCR:
			from .ocr_tesserocr import OCRTesserocr
			return OCRTesserocr()
		else:
			raise NotImplementedError
