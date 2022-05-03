#!/usr/bin/env python3
from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()


setup(
    name='dmax_dl',
    version='0.1.dev0',
    url='https://github.com/dr1s/dmax_dl.py',
    author='dr1s',
    author_email='dr1s@drs.li',
    license='MIT',
    description='Download series from dmax.de',
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['dmax_dl=dmax_dl:main']},
)
