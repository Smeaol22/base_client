# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='base_client',
    version='0.1.0',
    description='base client API package',
    long_description=readme,
    author='Dauloudet Olivier',
    url='https://github.com/Smeaol22/base_client.git',
    license=license,
    packages=find_packages(exclude='tests')
)