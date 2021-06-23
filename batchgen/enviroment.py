#!/usr/bin/env python3
#
# Sbatch enviroment
#
# Maintainer: glozanoa <glozanoa@uni.pe>

from collection import namedtuple

Variable = namedtuple("Variable", ['name', 'value'])

class SbatchEnviroment:
	def __init__(self, modules:List[str] = None,
	             variables:List[Variable] = None):
		self.modules = modules
		self.variables = variables

	def get_env(self):
		enviroment = []

		enviroment.append(modules)

		definition += (f"{variable.name}={variable.value}"
					   for variable in self.variables)

		enviroment.append(definition)

		return enviroment