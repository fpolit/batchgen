#!/usr/bin/env python3
#
# batchgen setup
#
# date: Feb 18 2021
# Maintainer: glozanoa <glozanoa@uni.pe>


from setuptools import setup, find_packages

VERSION = "0.0.5"

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()


setup(
    name='batchgen',
    version=VERSION,
    description='Slurm scripts generator',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords=['Slurm','Hpc Cluster'],
    author='glozanoa',
    author_email='glozanoa@uni.pe',
    url='https://github.com/fpolit/batchgen',
    license='GPL3',
    classifiers = [
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'tabulate'
    ],
 #   entry_points={
 #       'console_scripts':[
 #           'batchgen = batchgen.',
 #       ],
 #   }
)
