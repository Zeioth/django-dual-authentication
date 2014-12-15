#!/usr/bin/env python

from setuptools import setup


setup(
    name='django-dual-authentication',
    version='1.0.0',
    packages=['django-dual-authentication'],
    license='MIT',
    author='Zeioth',
    author_email='test@gmail.com',
    description='Allows authentication with either a username or an email address.',
    long_description='Allows authentication with either a username or an email address.',
    install_requires='',
    include_package_data=True,
    url='https://github.com/Zeioth/django-dual-authentication',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ]
)
