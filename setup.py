# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='granular_settings',
    version='0.0',
    packages=find_packages(where='src'),
    package_dir = {'': 'src'},
    author='Mikhail Petrov',
    author_email='mixael@yandex-team.ru',
    include_package_data = True,
)

