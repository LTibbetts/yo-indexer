"""Sets up the yo_indexer package"""
from setuptools import find_packages, setup

setup(name='yo_indexer',
      version='0.0.1',
      description='Imports a csv file and prints out the number of rows.' +
      'Additional information is given',
      url='www.example.com',
      author='Logan Tibbetts',
      author_email='Lcubed37@gmail.com',
      license='MIT',
      packages=find_packages(),
      package_data={'': ['*.csv']},
      zip_safe=False)
