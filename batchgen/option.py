#!/usr/bin/env python3
#
# Sbatch options
#
# Maintainer: glozanoa <glozanoa@uni.pe>


from typing import List, Any

class Option:
	def __init__(self, name: str, value_struct: Any, choices:List[Any] = None):
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
	
	def __repr__(self) -> str:
		return f"Option(name={self.name}, type={self.value_struct}, choices={self.choices}"

## VALIDATE THESE OPTIONS WITH PySlurm results
class SbatchOption:
	"""
	Sbatch Option
	"""
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
				choices=["block", "cyclic", "plane", "arbitrary"]),
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
		Option("threads-per-core", int),
		Option("verbose", bool),
		Option("nodelist", List[int]),
		Option("wait", bool)
	]

	def __init__(self, name:str, value:Any) -> None:
		self.option = SbatchOption.is_valid(name)
		self.name =	name

		# validate type of value with option.value_struct type
		if not self.has_valid_value(value):
			raise Exception(f"Invalid value for {name} SBATCH option")
		self.value = value


	@staticmethod
	def is_valid(name):
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
		if choices is not None:
			if isinstance(value, int) or \
				isinstance(value, str):
				if value not in choices:
					return  False

			if isinstance(value, list) or \
				isinstance(value, dict):
				all_valid = True
				for item in value:
					if item not in choices:
						all_invalid = False
						break

				if not all_invalid: # some invalid value
					return False

		# validate value_struct
		value_struct = self.option.value_struct
		# NOTE: Validate value_struct from typing module
		if (value_struct == bool and (not isinstance(value, bool))) or \
			(value_struct == str and (not isinstance(value, str))) or \
			(value_struct == int and (not isinstance(value, int))):
				return False

		return True

	def __repr__(self) -> str:
		if self.option.value_struct == bool:
			if self.value is True:
				return f"#SBATCH --{self.name}"
			else:
				return ''

		elif self.option.value_struct in [int, str]:
			return f"#SBATCH --{self.name}={self.value}"
		
		# these value_struct are mos complex (list or dictionary)
		# Check how to manage their values (MODIFY)
		else:
			return f"#SBATCH --{self.name}={self.value}"