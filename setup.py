#!/usr/bin/env python
from setuptools import setup, find_packages
import os
import sys

sys.path.insert(0,'TASSELpy')
#import release
#import TASSELpy
sys.path.pop(0)
#version = TASSELpy.__version__
packages = ['TASSELpy',
            'TASSELpy.java',
            'TASSELpy.java.lang',
            'TASSELpy.java.lang.reflect',
            'TASSELpy.java.util',
            'TASSELpy.data',
            'TASSELpy.net',
            'TASSELpy.net.maizegenetics',
            'TASSELpy.net.maizegenetics.analysis',
            'TASSELpy.net.maizegenetics.analysis.association',            
            'TASSELpy.net.maizegenetics.analysis.data',
            'TASSELpy.net.maizegenetics.analysis.distance',
            'TASSELpy.net.maizegenetics.analysis.popgen',
            'TASSELpy.net.maizegenetics.dna',
            'TASSELpy.net.maizegenetics.dna.map',
            'TASSELpy.net.maizegenetics.dna.snp',
            'TASSELpy.net.maizegenetics.dna.snp.depth',
            #'TASSELpy.net.maizegenetics.dna.snp.genotypecall',
            'TASSELpy.net.maizegenetics.dna.snp.score',
            'TASSELpy.net.maizegenetics.dna.tag',
            'TASSELpy.net.maizegenetics.matrixalgebra',
            'TASSELpy.net.maizegenetics.matrixalgebra.decomposition',
            'TASSELpy.net.maizegenetics.matrixalgebra.Matrix',
            'TASSELpy.net.maizegenetics.plugindef',
            'TASSELpy.net.maizegenetics.stats',
            'TASSELpy.net.maizegenetics.stats.statistics',
            'TASSELpy.net.maizegenetics.taxa',
            'TASSELpy.net.maizegenetics.taxa.distance',
            'TASSELpy.net.maizegenetics.trait',
            'TASSELpy.net.maizegenetics.util',
            'TASSELpy.utils',
            'TASSELpy.test',
            'TASSELpy.test.java',
            'TASSELpy.test.java.lang',
            'TASSELpy.test.java.util',
            'TASSELpy.test.net',
            'TASSELpy.test.net.maizegenetics',
            'TASSELpy.test.net.maizegenetics.analysis',
            'TASSELpy.test.net.maizegenetics.analysis.association',
            'TASSELpy.test.net.maizegenetics.analysis.distance',
            'TASSELpy.test.net.maizegenetics.analysis.popgen',
            'TASSELpy.test.net.maizegenetics.dna',
            'TASSELpy.test.net.maizegenetics.dna.snp',
            'TASSELpy.test.net.maizegenetics.dna.tag',
            'TASSELpy.test.net.maizegenetics.matrixalgebra',
            'TASSELpy.test.net.maizegenetics.matrixalgebra.Matrix',
            'TASSELpy.test.net.maizegenetics.matrixalgebra.decomposition',
            'TASSELpy.test.net.maizegenetics.stats',
            'TASSELpy.test.net.maizegenetics.stats.statistics',
            'TASSELpy.test.net.maizegenetics.taxa',
            'TASSELpy.test.net.maizegenetics.taxa.distance',
            'TASSELpy.test.net.maizegenetics.trait',
            'TASSELpy.test.net.maizegenetics.util',
            'TASSELpy.test.utils'
           ]
setup(
    name='tasselpy',
    version='0.20',
    author='Eli Rodgers-Melnick',
    author_email='er432@cornell.edu',
    description='A Python API for TASSEL',
    url='https://github.com/er432/TASSELpy',
    platforms=['Linux','Mac OSX', 'Windows', 'Unix'],
    keywords=['Genomics','Quantitative genetics', 'java'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ],
    packages=packages,
    package_data={'TASSELpy':['data/*.txt','lib/*']},
    license='BSD'
    )
# setup(
#     name = release.name.lower(),
#     version = version,
#     author = release.authors['Rodgers-Melnick'][0],
#     author_email = release.authors['Rodgers-Melnick'][1],
#     description = release.description,
#     keywords = release.keywords,
#     long_description = release.long_description,
#     license = release.license,
#     platforms = release.platforms,
#     url = release.url,
#     test_suite = 'TASSELpy.test',
#     classifiers = release.classifiers
#     )
