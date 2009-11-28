import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "tipi",
    version = "0.1",
    url = 'http://unbracketed.com/projects/tipi/',
    license = 'MIT',
    description = "Aims to provide conveniences for creating and managing Python virtualenvs",
    long_description = read('README'),
    keywords = 'utilities commands virtualenv packages modules installation deployment dependencies',
    author = 'Brian Luft',
    author_email = 'brian@unbracketed.com',

    packages = find_packages('tipi'),
    package_dir = {'': 'tipi'},

    install_requires = ['virtualenv','virtualenv-commands'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', 
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    scripts=['bin/tipi', 'bin/tipi-init',],
)

