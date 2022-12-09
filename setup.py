#!/usr/bin/env python

from setuptools import setup

setup(name='data_preprocessor',
      version='1.0',
      # list folders, not files
      packages=['utils.ticket_analysis'],
      package_data = {'setup': ['data/*'],'ticket_analysis': ['data/*']},
      scripts=[
          'utils/ticket_analysis/bin/ticket_analysis_processs_data.py',
      ],
      install_requires=[
          "pandas",
          "scrubadub",
          "textblob",
          "nltkdata",
          "setuptools",
          "openpyxl",
          "requests"
      ],
      )
