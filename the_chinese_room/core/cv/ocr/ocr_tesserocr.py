# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
	Huang Quanyong
	gzhuangquanyong@corp.netease.com
Date:
	2019/1/21
Description:
	ocr_tesserocr
----------------------------------------------------------------------------"""

import tesserocr

from .ocr import OCR

"""
TESSEROCR INSTALL
FOR WINDOWS:

A. install wheel file from https://github.com/simonflueckiger/tesserocr-windows_build/releases
B. clone 
	1. https://github.com/tesseract-ocr/tessdata.git or
	2. https://github.com/tesseract-ocr/tessdata_best.git or 
	3. https://github.com/tesseract-ocr/tessdata_fast.git 
into python.exe dir

"""


class OCRTesserocr(OCR):
	"""
	OCR using tesserocr module
	"""

	def __init__(self):
		pass

	def image_to_string(self, pil_image):
		return tesserocr.image_to_text(pil_image)
