# -*- coding: utf-8 -*-
"""Parker.

A web spider for collecting specific data
across a set of configured sites.
"""

import os
from setuptools import setup, find_packages
from pip.req import parse_requirements


def read(*names):
    """Read files for description."""
    values = dict()
    for name in names:
        filename = name + '.rst'
        if os.path.isfile(filename):
            fd = open(filename)
            value = fd.read()
            fd.close()
        else:
            value = ''
        values[name] = value
    return values


long_description = """
%(README)s

News
====

%(CHANGES)s

""" % read('README', 'CHANGES')

version_file = open('VERSION')
version = version_file.read().strip()

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='Parker',
    version=version,
    url='http://github.com/nefarioustim/parker/',
    license='GPL v3',
    author='Tim Huegdon',
    author_email='tim@nefariousdesigns.co.uk',
    description='A web spider for collecting specific data across a set of '
                'configured sites',
    long_description=long_description,
    install_requires=reqs,
    packages=['parker'],
    scripts=[
        'bin/parker-clean',
        'bin/parker-crawl',
        'bin/parker-config'
    ],
    include_package_data=True,
    zip_safe=False
)
