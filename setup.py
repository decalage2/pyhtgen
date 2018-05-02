#!/usr/bin/env python

'''
Setup script for pyhtgen
'''

# CHANGELOG
# 2009-03-02 v0.01: - 1st version
# 2010-05-25 v0.02: - renamed HTML.py to pyhtgen, package instead of module
# 2018-05-20 v0.5 - 
VERSION = '0.5'

long_description = ''' A Python module to easily generate HTML code (tables, lists, ...).
See http://www.decalage.info/python/html for more information. '''

from distutils.core import setup
import HTML

setup(name='pyhtgen',
      version='0.4',
      description='A Python module to easily generate HTML code (tables, lists, ...)',
      author='Philippe Lagadec',
      author_email='decalage (a) laposte.net',
      url='http://www.decalage.info/python/html',
      #py_modules = ['HTML']
      package_dir = {'pyhtgen': '.'}
      packages=['pyhtgen', 'HTML'],
     )
