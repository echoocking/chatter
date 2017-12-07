# Copyright (c) v87.us Development Team.

import os
import sys
from distutils.core import setup
from setuptools import find_packages

os.chdir(os.path.dirname(sys.argv[0]) or ".")
here = os.path.abspath(os.path.dirname(__file__))

ns = dict()
with open(os.path.join(here, 'version.py')) as f:
    exec(f.read(), dict(), ns)

setup_args = dict(
    name='chatter',
    version=ns['__version__'],
    description='Some descriptions',
    author='echoocking',
    license='WTF',
    url='git@github.com:echoocking/chatter.git',
    packages=find_packages(),
    include_package_data=True,
)

if 'setuptools' in sys.modules:
    setup_args['zip_safe'] = False
    setup_args['install_requires'] = install_requires = []

    with open('requirements.txt') as f:
        for line in f.readlines():
            req = line.strip()
            if not req or req.startswith('#') or '://' in req:
                continue
            install_requires.append(req)


def main():
    setup(**setup_args)


if __name__ == '__main__':
    main()