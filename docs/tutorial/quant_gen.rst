.. _quant_gen:

.. currentmodule:: TASSELpy

Running Quantitative Genetic Analyses
-------------------------------------

.. author, Eli Rodgers-Melnick

TASSELpy can run quantitative genetic analyses such as the GLM and the MLM in
the same way as the ordinary TASSEL API does. This approach uses plugins, which
don't have a very intuitive java interface. Because of this and the importance
of the quantitative genetic analyses, I've implemented convenience classes that
make performing quantitative genetics with TASSELpy much more intuitive than
the original java code would suggest.

Running the GLM
^^^^^^^^^^^^^^^

The generalized linear model plugin, used for a fixed effects analysis of phenotypes,
with or without non-marker covariates, is implemented in the 
:class:`TASSELpy.net.maizegenetics.analysis.association.FixedEffectLMPlugin.FixedEffectLMPlugin`
class. However, the more intuitive ``easy_GLM`` class can be imported using
:class:`TASSELpy.easy_GLM`. ``easy_GLM`` is actually a subclass of the 
``FixedEffectLMPlugin`` class, but its inputs and outputs are much more
straightforward. 

Below, I analyze the TASSEL tutorial data using the GLM with the ``easy_GLM``
class.

.. doctest::

    >>> from TASSELpy import TASSELbridge
    >>> TASSELbridge.start()
    >>> from TASSELpy.data.data_constants import *
    >>> from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
    >>> from TASSELpy.net.maizegenetics.trait.ReadPhenotypeUtils import ReadPhenotypeUtils
    >>> from TASSELpy.net.maizegenetics.analysis.association.FixedEffectLMPlugin import easy_GLM
    >>> inputAlign = ImportUtils.readFromHapmap(HAPMAP_FILE)
    Reading :/Users/eli/Development/TASSELpy/TASSELpy/data/mdp_genotype.hmp.txt  finished
    >>> traits = ReadPhenotypeUtils.readGenericFile(TRAITS_FILE)
    >>> pop = ReadPhenotypeUtils.readGenericFile(POP_STRUCTURE_FILE)
    >>> glm = easy_GLM()
    >>> glm.addPhenotype(traits,'traits')
    >>> glm.addMarkers(inputAlign,'markers')
    >>> glm.addCovariate(pop,'populations')
    >>> marker_effects, allele_effects = glm.run_glm(phenotypes=('traits',),markers='markers',covariates=('populations',))    

The two variables returned, ``marker_effects`` and ``allele_effects``, are actually
instances of
:class:`TASSELpy.net.maizegenetics.util.TableReport`. However, I have added a
convenience method to ``TableReport`` that returns a normal Python dictionary.

.. doctest::

   >>> marker_effects = marker_effects.toDict()
   >>> marker_effects.keys()
   ['marker_F', 'markerR2', 'modelMS', 'errorMS', 'Trait', 'modelDF', 'errorDF', 'Locus', 'Locus_pos', 'markerDF', 'marker_p', 'Marker', 'markerMS']
   >>> marker_effects['marker_p'][:10]
   [0.43840160640231907, 0.9416599121923893, 0.7049479924759525, 0.982243618828328, 0.8942029764864173, 0.1041698354391335, 0.6956794772390522, 0.8227948022963533, 0.23701678610514712, 0.8267525051080115]
