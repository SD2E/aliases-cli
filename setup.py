#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
# nifty - pull in __version__ from the code itself
from syd import __version__


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--ignore', 'build']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


def readme():
    with open('README.rst') as f:
        return f.read()


requires = [pkg for pkg in open('requirements.txt').readlines()]
requires_test = [pkg for pkg in open('requirements-travis.txt').readlines()]


setup(name='syd',
      version=__version__,
      description='Manages TACC Reactor and App alias mappings and ACLs',
      long_description=readme(),
      url='http://github.com/SD2E/aliases-cli',
      author='Matthew Vaughn',
      author_email='opensource@tacc.cloud',
      license='BSD',
      zip_safe=False,
      install_requires=requires,
      entry_points={
          'console_scripts': [
              'syd=syd.cli:main',
          ],
      },
      packages=find_packages(exclude=['docs', 'tests*']),
      classifiers=[
          'Intended Audience :: Developers',
          'Topic :: Utilities',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='cli',
      cmdclass={'test': PyTest},
      tests_require=requires_test,
      test_suite='tests')
