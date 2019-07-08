"""HelloWorld project."""

from setuptools import setup, find_packages

setup(
  name='helloworld',
  version='0.1.0',
  license='none',
  description='HelloWorld',

  author='scnsh',
  auther_email='aaaaa@bbbbb.com',
  url='https://github.com/scnsh/python-circlci-test',
  
  package=find_packages(where='src'),
  package_dir={'':'src'},

  install_requires=[],
  extras_require={},

  entry_points={
    'console_scripts': [
      'calclator = calclator',
    ]
  },
)