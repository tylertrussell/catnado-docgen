# modified from https://github.com/pypa/sampleproject


from setuptools import setup
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name='catnado-docgen',
  version='0.0.1dev1',
  description='A Python documentation utility.',
  long_description=long_description,
  url='http://github.com/tylertrussell/catnado-docgen',
  author='Tyler Trussell',
  author_email='tigertrussell+pip@gmail.com',
  license='Apache 2.0',
  keywords='python documentation generation mkdocs',
  packages=['catnado_docgen'],
  entry_points={
    'console_scripts': [
      'docgen = catnado_docgen.__main__:main',
    ],
  }
)
