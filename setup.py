from setuptools import setup, find_packages
import sys, os

version = '0.6b'
install_requires = [
	'argparse',
]
setup(name='redis-replay',
      version=version,
      description="A Redis event capture and replay utility",
      #long_description=open('README.md').read(),
      classifiers=['Topic :: Database',
                   'Topic :: Utilities',
                   'Topic :: System :: Systems Administration',
                   'Programming Language :: Python',],
      keywords='',
      author='Jesse Lesperance',
      author_email='jesse@jplesperance.me',
      url='http://gitlab.addsrv.com/jlesperance/redis-sa',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'redis-provision = bench.provision:main',
          ],
      },
      )
