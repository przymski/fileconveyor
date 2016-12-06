# coding=utf-8

# Python 2.5 compatibility.
from __future__ import with_statement

import os.path
import sys
from setuptools import setup, find_packages


VERSION = '0.5-dev'


def read_relative_file(filename):
    """Returns contents of the given file.
    Filename argument must be relative to this module.
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name='fileconveyor',
    version=VERSION,
    url='http://fileconveyor.org',
    download_url='https://github.com/piotrs-kainos/fileconveyor',
    author='Wim Leers',
    license='Unlicense',
    description="Daemon to detect, process and sync files to CDNs.",
    long_description=read_relative_file('README.txt'),
    platforms='Any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: Public Domain',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'setuptools==0.9.8',
        'cssutils==1.0.1',
        'boto==2.42.0',
        'python-cloudfiles==1.7.11',
        'Django==1.9.8',
        'django-cumulus==1.0.19',
        'django-storages==1.1.5'
    ] + (
        ["pyinotify==0.9.6"] if "linux" in sys.platform else []
    ),
)
