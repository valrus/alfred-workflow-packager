#!/usr/bin/env python
# coding=utf-8

from setuptools import setup


# Get long description (used on PyPI project page)
def get_long_description():
    try:
        # Use pandoc to create reStructuredText README if possible
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except:
        # Otherwise, default to using Markdown README
        with open('README.md', 'r') as readme_file:
            return readme_file.read()


setup(
    name='alfred-workflow-packager',
    version='0.12.0',
    description='A CLI utility for packaging and exporting Alfred workflows',
    long_description=get_long_description(),
    url='https://github.com/caleb531/alfred-workflow-packager',
    author='Caleb Evans',
    author_email='caleb@calebevans.me',
    license='MIT',
    keywords='alfred workflow package export',
    packages=['awp'],
    package_data={
        'awp': ['data/config-schema.json']
    },
    install_requires=[
        'biplist >= 1, < 2',
        'jsonschema >= 2, < 3'
    ],
    entry_points={
        'console_scripts': [
            'alfred-workflow-packager=awp.main:main',
            'workflow-packager=awp.main:main',
            'awp=awp.main:main'
        ]
    }
)
