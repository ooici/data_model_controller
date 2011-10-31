#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import os
import sys

if sys.platform == 'darwin':
    os.environ['C_INCLUDE_PATH'] = '/usr/local/include'

version = '0.1'

setup(  name = 'dataprocess',
        version = version,
        description = 'OOI ION Data Process base path',
        url = 'https://github.com/ooici/dataprocess',
        download_url = 'http://ooici.net/releases',
        license = 'Apache 2.0',
        author = 'David Stuebe',
        author_email = 'dstuebe@asascience.com',
        keywords = ['ooici','ioncore', 'pyon','streaming','data processing'],
        dependency_links = [
            'http://ooici.net/releases'
        ],
        test_suite = 'test',
        install_requires = [
            'simplejson==2.1.6',
            ##'msgpack-python==0.1.9',
            'setproctitle==1.1.2',
            'pyyaml==3.10',
            ##'pika==0.9.5',
            ##'httplib2==0.7.1',
            # 'pyzmq==2.1.7',
            ##'gevent_zeromq==0.2.0',
            ##'HTTP4Store==0.3.1',
            'zope.interface==3.6.4',
            ##'couchdb==0.8',
            # 'lockfile==0.9.1',
            ##'python-daemon==1.6',
            ##'bottle==0.9.6',
            ##'M2Crypto==0.21.1-pl1',
            'coverage==3.5',
            'nose==1.1.2',
            'ipython==0.11',
            'readline==6.2.1',
            # DM related dependencies for 'tables'
             'numpy==1.6.1',
             'numexpr==1.4.2',
             'cython==0.14.1',
            # Uncomment only after manually installing HDF5 package
            # see: http://www.hdfgroup.org/HDF5/release/obtain5.html
            'h5py==2.0.1',
            'tables==2.3',
        ],
     )
