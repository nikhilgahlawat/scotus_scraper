from setuptools import setup, find_packages

def read_requirements():
  with open('requirements.txt') as req_file:
    return req_file.readlines()

setup(
  name='scotus_scraper',
  version='0.1',
  packages=find_packages(where='src'),
  package_dir={'': 'src'},
  install_requires=read_requirements(),
  entry_points={
    'console_scripts': [
      'run-all=scripts.run_all:main',
    ],
  },
)
