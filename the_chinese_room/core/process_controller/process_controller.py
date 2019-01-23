# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
	Huang Quanyong
	gzhuangquanyong@corp.netease.com
Date:
	2019/1/23
Description:
	process_controller
----------------------------------------------------------------------------"""

import psutil
import subprocess
from the_chinese_room.utils.singleton import Singleton


class ProcessController(Singleton):
	def __init__(self):
		pass

	def start_progress(self, path):
		return subprocess.Popen(path)

	def get_pid_by_name(self, name):
		for p in psutil.process_iter():
			if p.name() == name:
				return p.pid

	def list_process_names(self):
		return tuple(p.name() for p in psutil.process_iter())