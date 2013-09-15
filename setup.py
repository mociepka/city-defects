#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup
from citydefects import __version__ as version

setup(name='city-defects',
      version=version,
      description='',
      author='Michał Ociepka',
      author_email='michal@ociepka.info',
      url='ociepka.info/city-defects',
      license='BSD',
      install_requires=[
          'Django>=1.6',
          'pillow>=2.1.0',
          'Unidecode>=0.04.13',
          'requests>=1.2.3',
          'djangorestframework>=2.3.8',
          'easy-thumbnails>=1.3'
      ],
      dependency_links=[
          'https://github.com/django/django/archive/1.6b3.tar.gz#egg=Django-1.6b3']
)
