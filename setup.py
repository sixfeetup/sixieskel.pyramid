from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='sixieskel.pyramid',
      version=version,
      description="Pyramid package skeletons for Six Feet Up",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web pyramid command-line skeleton project',
      author='Six Feet Up, Inc.',
      author_email='info@sixfeetup.com',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['sixieskel'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'templer.core'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      sfu_pyramid = sixieskel.pyramid.template:SixiePyramid
      [pyramid.scaffold]
      sfu_pyramid = sixieskel.pyramid.template:SixiePyramid
      """,
      )
