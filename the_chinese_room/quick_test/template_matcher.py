# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2019/1/19
Description:
    template_matcher.py
----------------------------------------------------------------------------"""

from the_chinese_room.core.cv.template_matcher import TemplateMatcher
from the_chinese_room.core.cv.cv_utils import mark_regions_in_pil_image

from PIL import Image


def test():
    tm = TemplateMatcher()
    image = Image.open("screenshot.png")
    template = Image.open("template.png")
    regions = tm.find_all(image, template)
    mark_regions_in_pil_image(image, regions)
    image.show()
