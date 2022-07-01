#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    path = os.path.join(package, "__init__.py")
    init_py = open(path, "r", encoding="utf8").read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_long_description():
    """
    Return the README.
    """
    return open("README.md", "r", encoding="utf8").read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]

env_marker_below_38 = "python_version < '3.8'"

minimal_requirements = [
    "click>=8.1.3",
    "colorama>=0.4.5"
]


setup(
    name="pycli",
    version=get_version("pycli"),
    url="https://github.com/JLRitch/starter-cli",
    license="BSD",
    description="Get started with a click cli.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Jere Ritchie",
    author_email="jereritchie@gmail.com",
    packages=get_packages("pycli"),
    python_requires=">=3.8",
    install_requires=minimal_requirements,
    include_package_data=True,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython"
    ],
    entry_points="""
    [console_scripts]
    pycli=pycli.main:app
    """,
    project_urls={
        "Source": "https://github.com/JLRitch/starter-cli"
    },
)