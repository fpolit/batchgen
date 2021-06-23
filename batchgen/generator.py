#!/usr/bin/env python3
#
# Sbatch script generator
#
# Maintainer: glozanoa <glozanoa@uni.pe>

from typing import List, Any
from tabulate import tabulate

from .option import SbatchOption
from .enviroment import SbatchEnviroment
from .job import Job


class BatchGenerator:
    """
    This class use sbatch options , enviroment and job to generate a batch script
    """
    def __init__(self, 
                    sbatch_options: List[SbatchOption] = [],
                    modules:List[str] = [], variables:List[dict] = {}, 
					env_module_system:str = 'spack',
                    jobs: List[str] = []):
        self.sbatch_options = sbatch_options
        self.enviroment = SbatchEnviroment(modules,variables, env_module_system)
        self.jobs = Job(jobs)
    
    def add_sbatch_option(self, name:str, value:Any):
        option = SbatchOption(name, value)
        self.sbatch_options.append(option)
        print(f"Added SBATCH option: {option}")

    def add_sbatch_options(self, sbatch_options:dict[str, Any]):
        for name, value in sbatch_options.items():
            option = SbatchOption(name, value)
            self.sbatch_options.append(option)
            print(f"Added SBATCH option: {option}")

    def show_sbatch_options(self):
        sbatch_options = [[option.name, option.value_struct, option.choices]
                            for option in SbatchOption.OPTIONS]

        print(tabulate(sbatch_options, headers=["Name", "Type", "Choices"]))

    def generate(self, script_name:str):
        with open(script_name, 'w') as batch_script:
            batch_script.write("#!/bin/bash\n")

            # writing sbatch options
            for sbatch_option in self.sbatch_options:
                batch_script.write(f"{sbatch_option}\n")

            batch_script.write("\n")
            # writing enviroment (pre load modules cmds + load modules + variable definition)
            for env_block in self.enviroment.get_env():
                for env_cmd in env_block:
                    batch_script.write(f"{env_cmd}\n")
                batch_script.write("\n")


            batch_script.write("\n")
            # writing body (jobs)
            for job_block in self.jobs.get_job():
                for job in job_block:
                    batch_script.write(f"{job}\n")
                batch_script.write("\n")

        print(f"Batch script was generated: {script_name}")