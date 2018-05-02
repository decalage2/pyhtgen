"""
Setup script for pyhtgen
"""

# CHANGELOG
# 2009-03-02 v0.01: - 1st version
# 2010-05-25 v0.02: - renamed HTML.py to pyhtgen, package instead of module

import distutils.core
import HTML

DESCRIPTION = """A Python module to easily generate HTML code (tables, lists, ...).
See http://www.decalage.info/python/html for more information.
"""

kw = {
    'name': "pyhtgen",
    'version': HTML.__version__,
    'description': DESCRIPTION,
    'author': "Philippe Lagadec",
    'author_email': "decalage (a) laposte.net",
    'url': "http://www.decalage.info/python/html",
    'license': "CeCILL (open-source GPL compatible)",
    'py_modules': ['HTML']
    'package_dir': {'pyhtgen': '.'},
    'packages': ['pyhtgen'],
    }


# If we're running Python 2.3+, add extra information
if hasattr(distutils.core, 'setup_keywords'):
    if 'classifiers' in distutils.core.setup_keywords:
        kw['classifiers'] = [
            'Development Status :: 4 - Beta',
            #'License :: Freely Distributable',
            'Natural Language :: English',
            'Intended Audience :: Developers',
            'Topic :: Internet :: WWW/HTTP',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules'
          ]
    if 'download_url' in distutils.core.setup_keywords:
        kw['download_url'] = "http://www.decalage.info/python/html"


distutils.core.setup(**kw)
