from rbco.rename import console
from setuptools import setup, find_packages
import os

version = '0.1'

script_functions = [getattr(console, f) for f in dir(console)]
script_functions = [
    f for f in script_functions 
    if getattr(f, '__doc__', None) and ('Usage: ' in 'Usage: ' in f.__doc__)
]
console_scripts = [
    '%(func)s = rbco.rename.console:%(func)s' % {'func': f.__name__}
    for f in script_functions
]

usage_doc = \
"""
Usage
=====

"""

for f in script_functions:
    usage_doc += '- %s\n' % f.__doc__.replace('Usage: ', '')



setup(name='rbco.rename',
      version=version,
      description="A set of Python scripts to rename files in batch.",
      long_description=open("README.txt").read() + "\n" + usage_doc + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='shell unix filesystem',
      author='Rafael Oliveira',
      author_email='rafaelbco@gmail.com',
      url='',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rbco'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points={'console_scripts': console_scripts},
)
