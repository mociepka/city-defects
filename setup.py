#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup

setup(name='city-defects',
      version='1.0a1',
      description='',
      author='Michał Ociepka',
      author_email='michal@ociepka.info',
      url='ociepka.info/city-defects',
      license='BSD',
      install_requires=['Django>=1.6', 'pillow>=2.1.0'],
      dependency_links=[
          'https://github.com/django/django/archive/1.6b1.tar.gz#egg=Django-1.6b1']
)
