from setuptools import setup, find_packages
import sys, os

version = '0.3'

setup(name='Pycheat',
      version=version,
      description="Python Cheat Scripts for Systems Administrators and Alike",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='systems administration python script administration',
      author='Ozgur Ozdemircili',
      author_email='ozdemircili@gmail.com',
      url='http://www.codensys.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
