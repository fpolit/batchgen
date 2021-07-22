#!/usr/bin/env python3
#
# Job to perform inside batch script
#
# Maintainer: glozanoa <glozanoa@uni.pe>

import os
from typing import List

class Job:
	def __init__(self):
		self.jobs = []

	def add_job(self, job:str):
		self.jobs.append(job)

	def add_job_block(self, job_block:List[str]):
		self.jobs.append(job_block)
	
	def add_bash_block(self, bash_script:str):
		if not os.path.isfile(bash_script):
			raise Exception(f"{bash_script} is not a file")

		job_block = []
		with open(bash_script, 'r') as bash:
			while cmd := bash.readline():
				cmd = cmd.rstrip()
				if cmd not in ["#!/bin/bash", "#!/bin/sh", '']:
					job_block.append(cmd)
		
		self.add_job_block(job_block)

	def get_job(self):
		blocks = {}
		block_id = 0

		for job in self.jobs:
			if isinstance(job, list) or \
				isinstance(job, tuple): #this is a block of job
				block_id += 1
				blocks[block_id] = job
				block_id += 1
			else:
				if block_id not in blocks:
					blocks[block_id] = [job]
				else:
					blocks[block_id].append(job)
		
		return list(blocks.values())
