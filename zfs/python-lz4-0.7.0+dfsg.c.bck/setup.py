#!/usr/bin/env python


from setuptools import setup, find_packages, Extension

VERSION = (0, 7, 0)
VERSION_STR = ".".join([str(x) for x in VERSION])

setup(
    name='lz4zfs',
    version=VERSION_STR,
    description="LZ4 Bindings for Python",
    long_description=open('README.rst', 'r').read(),
    author='Steeve Morin',
    author_email='steeve.morin@gmail.com',
    url='https://github.com/steeve/python-lz4zfs',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    ext_modules=[
        Extension('lz4zfs', [
            'src/python-lz4zfs.c'
        ], extra_compile_args=[
            "-std=c99",
            "-O3",
            "-Wall",
            "-W",
            "-Wundef",
            "-DVERSION=\"%s\"" % VERSION_STR,
            "-DLZ4_VERSION=\"r119\"",
        ])
    ],
    setup_requires=["nose>=1.0"],
    test_suite = "nose.collector",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
)
