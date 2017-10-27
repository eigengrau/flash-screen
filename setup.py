#!/usr/bin/env python

import subprocess
import shlex
from setuptools import setup

version = '0.2.1.0'

try:
    hash = (
        subprocess
        .check_output(shlex.split('git rev-parse --short HEAD'))
        .rstrip()
        .decode('ASCII')
    )
    commit = (
        subprocess
        .check_output(shlex.split('git rev-list --count HEAD'))
        .rstrip()
        .decode('ASCII')
    )
except:
    pass
else:
    version = '{}.dev{}+{}'.format(version, commit, hash)


setup(
    name='flash-screen',
    version=version,
    description="screen-flash makes the screen flash",
    author="Sebastian Reuße",
    author_email='seb@wirrsal.net',
    url='https://github.com/eigengrau/flash-screen',
    packages=['flash_screen'],
    package_dir={'': 'src'},
    install_requires=['pygobject >= 3.18, < 3.27'],
    license="GPL3",
    entry_points={
        'console_scripts': [
            'flash-screen = flash_screen.cli:console_entry'
        ],
    }
)
