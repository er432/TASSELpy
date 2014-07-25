#!/usr/bin/env python
from setuptools import setup, find_packages
import os
import sys

sys.path.insert(0,'TASSELpy')
import release
sys.path.pop(0)
version = release.write_versionfile()
packages = ['TASSELpy',
            'TASSELpy.java',
            'TASSELpy.java.lang',
            'TASSELpy.java.lang.reflect',
            'TASSELpy.java.util',
            'TASSELpy.data',
            'TASSELpy.lib',
            'TASSELpy.net',
            'TASSELpy.net.maizegenetics',
            'TASSELpy.net.maizegenetics.distance',
            'TASSELpy.net.maizegenetics.popgen',
            'TASSELpy.net.maizegenetics.map',
            'TASSELpy.net.maizegenetics.snp',
            'TASSELpy.net.maizegenetics.snp.depth',
            'TASSELpy.net.maizegenetics.snp.genotypecall',
            'TASSELpy.net.maizegenetics.snp.score',
            'TASSELpy.net.maizegenetics.tag',
            'TASSELpy.net.maizegenetics.matrixalgebra',
            'TASSELpy.net.maizegenetics.matrixalgebra.decomposition',
            'TASSELpy.net.maizegenetics.matrixalgebra.Matrix',
            'TASSELpy.net.maizegenetics.stats',
            'TASSELpy.net.maizegenetics.stats.statistics',
            'TASSELpy.net.maizegenetics.taxa',
            'TASSELpy.net.maizegenetics.taxa.distance',
            'TASSELpy.net.maizegenetics.trait',
            'TASSELpy.net.maizegenetics.util'
           ]
setup(
    name = release.name.lower(),
    version = version,
    author = release.authors['Rodgers-Melnick'][0],
    author_email = release.authors['Rodgers-Melnick'][1],
    description = release.description,
    keywords = release.keywords,
    long_description = release.long_description,
    license = release.license,
    platforms = release.platforms,
    url = release.url,
    test_suite = 'TASSELpy.test',
    classifiers = release.classifiers
    )
