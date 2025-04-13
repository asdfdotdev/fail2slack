#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fail2slack',
    version='0.5.0',
    description='Send fail2ban jail status updates to Slack.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GPL-2.0',
    packages=find_packages(),
    author='Chris Carlevato',
    author_email='hello@asdf.dev',
    keywords=['fail2ban', 'slack'],
    url='https://github.com/asdfdotdev/fail2slack',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Security",
        "Topic :: System",
        "Topic :: Utilities",
    ],
    install_requires=[
        'argparse==1.4.0',
        'requests==2.32.3',
        'validators==0.34.0',
    ],
)
