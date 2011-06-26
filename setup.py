from setuptools import setup, find_packages
import os

version = '0.4'

setup(name='rbco.rename',
      version=version,
      description="A set of Python scripts to rename files in batch.",
      long_description=open("README.txt").read() + "\n" +
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
          'Unidecode',
      ],
      entry_points={
          'console_scripts': [
              'renpre = rbco.rename.console:renpre',
              'rensuf = rbco.rename.console:rensuf',
              'unhide = rbco.rename.console:unhide',
              'renlu = rbco.rename.console:renlu',
              'renmp3 = rbco.rename.console:renmp3',
              'renid3 = rbco.rename.console:renid3',              
              'renrep = rbco.rename.console:renrep',                    
              'rendeln = rbco.rename.console:rendeln',                    
              'rendel = rbco.rename.console:rendel',      
              'renremoveacc = rbco.rename.console:renremoveacc',
          ]
      },
)
