"""
A full-screen image modal XBlock
"""
from os import path
from setuptools import setup


version = '1.0.1'
description = __doc__.strip().split('\n')[0]
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst')) as file_in:
    long_description = file_in.read()

setup(
    name='xblock-image-modal',
    version=version,
    description=description,
    long_description=long_description,
    author='stv',
    author_email='stv@stanford.edu',
    url='https://github.com/Stanford-Online/xblock-image-modal',
    license='AGPL-3.0',
    packages=[
        'imagemodal',
    ],
    install_requires=[
        'Django<2.0.0',
        'edx-opaque-keys',
        'mock',
        'six',
        'XBlock',
        'xblock-utils',
    ],
    entry_points={
        'xblock.v1': [
            'imagemodal = imagemodal.xblocks:ImageModal',
        ],
    },
    package_dir={
        'imagemodal': 'imagemodal',
    },
    package_data={
        "imagemodal": [
            'mixins/*.py',
            'public/*',
            'scenarios/*.xml',
            'templates/*',
            'translations/*/*/*',
        ],
    },
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Topic :: Education',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='imagemodal.tests',
)
