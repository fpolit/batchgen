#!/usr/bin/env python3
#
# Sbatch enviroment
#
# Maintainer: glozanoa <glozanoa@uni.pe>

from typing import List

class SbatchEnviroment:
	ENV_MODULE_SYSTEMS = ['spack', 'lmod']

	def __init__(self, modules:List[str] = [], variables:List[dict] = {}, 
					env_module_system:str = 'spack'):

		if env_module_system not in SbatchEnviroment.ENV_MODULE_SYSTEMS:
			raise Exception(f"Unsupported enviroment module system: {env_module_system}")

		self.env_module_system = env_module_system

		self.enviroment = {'pre_load':[], 'modules': {}, 'variables': {}}
		self.load_modules(modules)
		self.define_variables(variables)

	def pre_modules_load(self, cmd:str):
		self.enviroment['pre_load'].append(cmd)

	def unload_module(self, module:str):
		if module in self.enviroment['modules']:
			del self.enviroment['modules'][module]
			print(f"Module {module} was unload")
		else:
			raise Exception(f"No {module} module was loaded")

	def load_modules(self, modules:List[str]):
		if self.env_module_system == 'spack':
			for module in modules:
				self.enviroment["modules"][module] = f"spack load {module}"
				print(f"Module {module} was load")
		else:
			for module in modules:
				self.enviroment["modules"][module] = f"module load {module}"
				print(f"Module {module} was load")

	
	def delete_variable(self, variable:str):
		if  variable in self.enviroment["variables"]:
			del self.enviroment['variables'][variable]
			print(f"Variable {variable} was deleted")
		else:
			raise Exception(f"No {variable} variable was defined")

	def define_variables(self, variables:dict[str, str]):
		for name, value in variables.items():
			self.enviroment["variables"][name] = f"{name}={value}"
			print(f"Variable {name} was defined")

	def get_env(self):
		"""
		Return a list of 3 block: a block of comand to be executed before load modules, 
		other block of commands to load modules and other of variables definitions
		"""
		enviroment = []

		enviroment.append(self.enviroment['pre_load'])
		
		modules = list(self.enviroment["modules"].values())
		enviroment.append(modules)

		variables = list(self.enviroment["variables"].values())
		enviroment.append(variables)

		return enviroment
