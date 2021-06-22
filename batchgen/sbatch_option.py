#!/usr/bin/env python3

from typing import List, Any

class Option:
	def __init__(name: str, value_struct: Any, choices:List[Any] = None):
		"""
		value_struct: is the expected structure that its value will have
		choices:
		If the option has a simple value then choices variable
		has the posible values, but if it is a dictionary,
		then choices variable has the possible values for its keys
		"""
		self.name = name
		self.value_struct = value_struct
		self.choices = choices


class SbatchOption:
	# NOTE VALIDATE THESE OPTIONS WITH PySlurm results
	OPTIONS = [
		Option("array", Any),
		Option("account",str),
		Option("acctg-freq", dict[str, Any],
		       choices=['tasks', 'energy', 'network', 'filesystem']),
		Option("extra-node-info", Any),
		Option("batch", List[str]),
		Option("bb", Any),
		Option("bbf", Any),
		Option("begin", str),
		Option("cluster-constraint", List[Any]),
		Option("comment", str),
		Option("constraint", Any),
		Option("contiguous", bool),
		Option("cores-per-socket", int),
		Option("cpu-freq", Any),
		Option("cpus-per-gpu", int),
		Option("cpus-per-task", int),
		Option("deadline", Any),
		Option("delay-boot", int),
		Option("dependency", dict[str, List[int]],
		       choices=['after', 'afterany', 'afterburstbuffer',
		                'aftercorr', 'afternotok', 'afterok',
		                'expand']),
		Option("chdir", str),
		Option("error", str),
		Option("exclucive", str, choices=['user', 'mcs']),
		Option("export", List[Any]),
		Option("export-file", str),
		Option("nodefile", str),
		Option("get-user-env", str),
		Option("gid", int),
		Option("gpus", dict[str, int]),
		Option("gpu-bind", dict[str, Any]),
		Option("gpu-freq", Any),
		Option("gpus-per-node", dict[str, int]),
		Option("gpus-per-socket", dict[str, int]),
		Option("gpus-per-task", dict[str, int]),
		Option("gres", List[Any]),
		Option("gres-flags", str,
		       choices=['disable-binding', 'enforce-binding']),
		Option("hold", int),
		Option("hint", str,
		       choices=["compute_bound", "memory_bound",
		                "multithread", "nomultithread"]),
		Option("ignore-pbs", bool),
		Option("input", str),
		Option("job-name", str),
		Option("no-kill", bool),
		Option("clusters", str),
		Option("distribution", str,
		       choices=["block", "cyclic", "plane", "arbitrary"])m
		Option("mail-type", str,
		       choices=["BEGIN", "END", "FAIL", "INVALID_DEPEND",
		                "REQUEUE", "STAGE_OUT", "ALL", "TIME_LIMIT",
		                "TIME_LIMIT_90", "TIME_LIMIT_80",
		                "TIME_LIMIT_50", "ARRAY_TASKS"]),
		Option("mail-user", str),
		Option("mem", str),
		Option("mem-per-cpu", str),
		Option("mem-per-gpu", str),
		Option("mincpus", str),
		Option("nodes", str),
		Option("ntasks", int),
		Option("network", str),
		Option("nice", int),
		Option("no-requeue", bool),
		Option("ntasks-per-core", int),
		Option("ntasks-per-gpu", int),
		Option("ntasks-per-node", int),
		Option("ntasks-per-socket", int),
		Option("overcommit", bool),
		Option("output", str),
		Option("open-mode", str,
		       choices=["append", "truncate"]),
		Option("partition", str),
		Option("power", List[str]),
		Option("quiet", bool),
		Option("requeue", bool),
		Option("time", str),
		Option("test-only", bool),
		Option("verbose", bool),
		Option("nodelist", List[int]),
		Option("wait", bool)
	]

	def __init__(self, name, value):
		self.option = SbatchOption.is_valid(name)

		self.name =	name

		# validate type of value with option.value_struct type
		if not SbatchOption.has_valid_value(value):
			raise Exception("Invalid value for {name} SBATCH option")
		self.value = value


	def is_valid(self, name):
		any_valid = False
		for option in SbatchOption.OPTIONS:
			if option.name == name:
				any_valid = True
				break

		if not any_valid:
			raise Exception(f"Invalid SBATCH option: {name}")

		return option

	def has_valid_value(self, value):
		choices = self.option.choices
		if choices not is None:
			if isinstance(value, int) or \
			   isinstance(value, str):
				if value not in choices:
					return  False
			if isinstance(value, list) or \
			   isinstance(value, dict):
				no_invalid = True
				for item in value:
					if item not in choices:
						no_invalid = False
						break

				if not no_invalid: # some invalid value
					return False

		return True
