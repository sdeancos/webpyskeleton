#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


from app import config

setup(
    name='webpyskeleton',
    version=config.__version__,
    description='web.py skeleton (web.py + routing json + jinja2)',
    packages=['app'],
    url='https://github.com/sdeancos/webpyskeleton',
    license='Public domain',
    author='Samuel de Ancos',
    author_email='sdeancos@gmail.com',
    maintainer='Samuel de Ancos',
    maintainer_email='sdeancos@gmail.com',
    scripts=['app/bin/wps_create_project.py'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['web.py','Jinja2', '_mysql'],
    requires=['web.py','Jinja2', '_mysql'],
)