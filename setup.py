#!/usr/bin/env python
# -*- coding: utf-8
from sys import version_info
from setuptools import setup

setup(
    name='damask_plot',
    version='0.1.0',
    description='Düsseldorf Advanced Material Simulation Kit (DAMASK) "live plotter" for Jupyter',
    author='Lukas Koschmieder; Mingxuan Lin',
    author_email='lukas.koschmieder@rwth-aachen.de',
    license='MIT',
    url='https://github.com/lukas-koschmieder/damask_plot',
    requires=['aixplot', 'parsimonious'],
    packages=['damask_plot'],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: End Users',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development'],
    keywords=['DAMASK', 'Plot', 'Visualization', 'Jupyter', 'JupyterLab', 'Widget'],
)
