# setup.py

from setuptools import setup

setup(
   name='enginepy',
   version='1.0.4',
   description='A simple and powerful python API for running external commands.',
   license="Mozilla Public License 2.0 (MPL 2.0)",
   long_description='A simple and powerful python API for external commands. Arguments toggle the behavior of STDOUT and STDERR. The return code is always available.',
   author='Phenicle',
   author_email='pheniclebeefheart@gmail.com',
   url="https://github.com/phenicle/enginepy",
   packages=['enginepy',],  #same as name
   install_requires=[], #external packages as dependencies
)
