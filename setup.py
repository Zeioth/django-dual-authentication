#!/usr/bin/env python

from setuptools import setup

try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    description = open('README.md').read()


setup(
    name='django-dual-authentication',
    version='0.4.0',
    packages=['django-dual-authentication'],
    license='MIT',
    author='Zeioth',
    author_email='test@gmail.com',
    description='Allows authentication with either a username or an email address.',
    long_description=description,
    install_requires='',
    include_package_data=True,
    url='https://github.com/Zeioth/django-dual-authentication',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
