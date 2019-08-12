#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fail2slack',
    version='0.1',
    description='Send fail2ban status updates to Slack.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GPL-2.0',
    packages=find_packages(),
    author='Chris Carlevato',
    author_email='hello@asdf.dev',
    keywords=['fail2ban', 'slack'],
    url='https://github.com/asdfdotdev/fail2slack',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'argparse==1.4.0',
        'requests==2.22.0',
        'validators==0.13.0',
    ],
)
