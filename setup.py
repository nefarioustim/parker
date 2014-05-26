"""
Parker
-----

Parker is a Python-based web spider for collecting specific data across a set
of configured sites.

"""

from setuptools import setup
from pip.req import parse_requirements

version_file = open(os.path.join(mypackage_root_dir, 'VERSION'))
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
    long_description=__doc__,
    install_requires=reqs
)