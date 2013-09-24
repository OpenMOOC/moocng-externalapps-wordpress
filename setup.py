# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

VERSION = '0.1.0'

setup(
    name='moocng-externalapps-wordpress',
    version=VERSION,
    url='https://github.com/OpenMOOC/moocng-externalapps-wordpress',
    description=('MOOC plugin'),
    long_description=(read('README.md') + '\n\n' + read('CHANGES')),
    author='Yaco Sistemas',
    classifiers=[
        'Development Status :: 6 - Development',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['moocng'],
    entry_points = """
        [moocng.externalapp]
        wordpress = moocngwordpress.wordpress:Wordpress
    """,
)
