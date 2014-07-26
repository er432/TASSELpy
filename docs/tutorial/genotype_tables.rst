.. _genotype_tables:

.. currentmodule:: TASSELpy

Loading and Manipulating GenotypeTables
---------------------------------------

.. author, Eli Rodgers-Melnick

Loading genetic polymorphism data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The easiest way to load polymorphism data is to use the ``readGuessFormat`` function in the
:class:`TASSELpy.net.maizegenetics.dna.snp.ImportUtils.ImportUtils` class. This class also has 
several other methods to load specific file flormats. Here, I use the ``readGuessFormat`` function
to load in the top few lines of the TASSEL tutorial data, which is stored in 
:mod:`TASSELpy.data`.

.. doctest::

   >>> from TASSELpy import TASSELbridge
   >>> TASSELbridge.start()
   >>> from TASSELpy.data import data_constants
   >>> from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
   >>> data = ImportUtils.readGuessFormat(data_constants.SHORT_HMP_FILE)

Using the GenotypeTable
^^^^^^^^^^^^^^^^^^^^^^^

``ImportUtils`` loads the polymorphism data into a 
:class:`TASSELpy.net.maizegenetics.dna.snp.CoreGenotypeTable` object. Like all wrapped TASSEL
classes, this carries all the functions available in the Java API. It carries a large number
of functions that can be used to summarize the data.

.. doctest::
   
   >>> data.numberOfSites()
   9
   >>> data.numChromosomes()
   1
   >>> data.genotypeAsStringRow(0)
   u'C;C;G;T;G;T;G;T;C'
   >>> data.genotypeAsStringRow(1) 
   u'C;G;G;T;G;T;C;T;C'

Filtering the GenotypeTable
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Filtering of the GenotypeTable can be done using the 
:class:`TASSELpy.net.maizegenetics.dna.snp.FilterGenotypeTable.FilterGenotypeTable` class. While this class
does provide the basic methods available in the Java API, it also adds some functional
programming aspects that could not be implemented in Java (at least prior to version 8).
Below, I use functional programming - provided by the 
:meth:`TASSELpy.net.maizegenetics.dna.snp.FilterGenotypeTable.FilterGenotypeTable.fuctionalFilters`
function - to filter the data to taxa with the first character '3' and that are on chromosome
1. The ``functionalFilters`` function takes callable arguments in either the ``sitesFilter`` keyword, the
``taxaFilter`` keyword, or both. Callables passed into the ``sitesFilter`` function receive a
:class:`TASSELpy.net.maizegenetics.dna.map.Position` object, while callables passed into the
``taxaFilter`` function receive a
:class:`TASSELpy.net.maizegenetics.taxa.Taxon.Taxon` object. A given Taxon/Postion is retained
if the function returns `True` for that object.

.. doctest::

   >>> [x for x in data.taxa()][:10]
   [Taxon(33-16), Taxon(38-11), Taxon(4226), Taxon(4722), Taxon(A188), Taxon(A214N), 
   Taxon(A239), Taxon(A272), Taxon(A441-5), Taxon(A554)]
   >>> from TASSELpy.net.maizegenetics.dna.snp.FilterGenotypeTable import FilterGenotypeTable
   >>> filtered = FilterGenotypeTable.functionalFilters(data,
   ... sitesFilter=lambda x: x.getChromosome().getName() == '1',
   ... taxaFilter=lambda x: x.getName().startswith('3'))
   >>> [x for x in filtered.taxa()]
   [Taxon(33-16), Taxon(38-11)]
   >>> filtered.numberOfSites()
   9


