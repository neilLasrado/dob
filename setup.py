# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='dob',
    version=version,
    description='Directory data collection for Rotary 3142',
    author='Neil Trini Lasrado',
    author_email='nlasrado@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
