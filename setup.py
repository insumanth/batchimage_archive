#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'opencv-python' , 'tqdm' ]

test_requirements = ['pytest>=3', ]

setup(
    author="Sumanth",
    author_email='sumanthreddystar@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Batch Image Processing",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='batchimage',
    name='batchimage',
    packages=find_packages(include=['batchimage', 'batchimage.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/insumanth/batchimage',
    version='0.1.2',
    zip_safe=False,
)
