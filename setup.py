# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='agilent_34411A',
      version = '0.2.0',
      description = 'Interface to the table-top DMM Agilent 34411A via TCP/IP',
      long_description = '',
      author = 'Philipp Klaus',
      author_email = 'klaus@physik.uni-frankfurt.de',
      url = '',
      license = 'GPL',
      packages = ['agilent_34411A'],
      scripts = ['scripts/agilent_34411A_cli'],
      zip_safe = True,
      platforms = 'any',
      keywords = 'Agilent 34411A DMM',
      classifiers = [
          'Development Status :: 4 - Beta',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GPL License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Topic :: System :: Monitoring',
          'Topic :: System :: Logging',
      ]
)


