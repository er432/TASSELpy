from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload, javaStaticOverload
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.String import metaString
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.net.maizegenetics.dna.snp.genotypecall.GenotypeMergeRule import GenotypeMergeRule
from TASSELpy.net.maizegenetics.dna.GenotypeTable import GenotypeTable
from TASSELpy.net.maizegenetics.dna.snp.genotypecall.GenotypeCallTable import GenotypeCallTable
from TASSELpy.net.maizegenetics.dna.map.PositionList import PositionList
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
from TASSELpy.net.maizegenetics.dna.snp.score.AlleleProbability import AlleleProbability
from TASSELpy.net.maizegenetics.dna.snp.depth.AlleleDepth import AlleleDepth
from TASSELpy.net.maizegenetics.dna.snp.score.Dosage import Dosage
from TASSELpy.net.maizegenetics.util.GeneralAnnotationStorage import GeneralAnnotationStorage
from TASSELpy.net.maizegenetics.dna.snp.score.ReferenceProbability import ReferenceProbability

java_imports = {'AlleleDepth':'net/maizegenetics/dna/snp/depth/AlleleDepth',
                'AlleleProbability':'net/maizegenetics/dna/snp/score/AlleleProbability',
                'Dosage':'net/maizegenetics/dna/snp/score/Dosage',
                'GeneralAnnotationStorage':'net/maizegenetics/util/GeneralAnnotationStorage',
                'GenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/GenotypeCallTable',
                'GenotypeMergeRule':'net/maizegenetics/dna/snp/genotypecall/GenotypeMergeRule',
                'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
                'GenotypeTableBuilder':'net/maizegenetics/dna/snp/GenotypeTableBuilder',
                'PositionList':'net/maizegenetics/dna/map/PositionList',
                'ReferenceProbability':'net/maizegenetics/dna/snp/score/ReferenceProbability',
                'String':'java/lang/String',
                'TaxaList':'net/maizegenetics/taxa/TaxaList'}
class GenotypeTableBuilder(Object):
    """ Builder for GenotypeTables

    New genotypeTables are built from a minimum of TaxaList, PositionList,
    and GenotypeCallTable. Depth and Scores are optional features of GenotypeTables.

    If you know the taxa, position, and genotypes are known from the beginning,
    use GenotypeTable(a = GenotypeTableBuilder.getInstance(genotype, positionList, taxaList))

    In many situations, only GenotypeTables are built incrementally, either by Taxa or Site

    In many cases, genotype want to add taxa to an existing genotypeTable. Direct
    addition is not possible, as GenotypeTables are immutable, but the
    GenotypeTableBuilder.getTaxaIncremental provides a strategy for creating and merging taxa
    together. Key to the process is that GenotypeMergeRule defines how the taxa with identical
    names will be merged. Merging is possible with HDF5 files, but only if the closeUnfinished() method
    was used with the previous building
    """
    _java_name = java_imports['GenotypeTableBuilder']
    @javaConstructorOverload(java_imports['GenotypeTableBuilder'])
    def __init__(self, *args, **kwargs):
        pass
    @javaStaticOverload(java_imports['GenotypeTableBuilder'], 'getBuilder',
                        (make_sig([java_imports['String']], java_imports['GenotypeTableBuilder']),
                         (metaString), lambda x: GenotypeTableBuilder(obj=x)))
    def getBuilder(*args):
        """ Returns a builder to an existing, unfinished HDF5 genotypes file

        Can be used if you want to add/modify annotations, etc, and/or
        call build() to finalize it

        Signatures:

        static GenotypeTableBuilder getBuilder(String existingHDF5File)

        Arguments:

        existingHDF5File -- The name of the HDF5 file containining the genotypes

        Returns:

        A GenotypeTableBuilder working off of the existing genotypes
        in the HDF5 file
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableBuilder'],"getTaxaIncremental",
                        (make_sig([java_imports['PositionList']],java_imports['GenotypeTableBuilder']),
                         (PositionList,), lambda x: GenotypeTableBuilder(obj=x)),
                         (make_sig([java_imports['PositionList'],java_imports['GenotypeMergeRule']],
                                   java_imports['GenotypeTableBuilder']),(PositionList,GenotypeMergeRule),
                         lambda x: GenotypeTableBuilder(obj=x)),
                         (make_sig([java_imports['GenotypeTable'],java_imports['GenotypeMergeRule']],
                                   java_imports['GenotypeTableBuilder']),(GenotypeTable, GenotypeMergeRule),
                         lambda x: GenotypeTableBuilder(obj=x)),
                         (make_sig([java_imports['PositionList'],java_imports['String']],
                                   java_imports['GenotypeTableBuilder']), (PositionList, metaString),
                         lambda x: GenotypeTableBuilder(obj=x)))
    def getTaxaIncremental(*args):
        """ Creates a builder allowing addition by taxa.

        Signatures:

        static GenotypeTableBuilder getTaxaIncremental(PositionList positionList)
        static GenotypeTableBuilder getTaxaIncremental(PositionList positionList, GenotypeMergeRule mergeRule)
        static GenotypeTableBuilder getTaxaIncremental(GenotypeTable genotypeTable, GenotypeMergeRule mergeRule)
        static GenotypeTableBuilder getTaxaIncremental(PositionList positionList, String newHDF5File)

        Arguments:

        static GenotypeTableBuilder getTaxaIncremental(PositionList positionList)
            positionList -- The positions used for the builder
        static GenotypeTableBuilder getTaxaIncremental(PositionList positionList, GenotypeMergeRule mergeRule)
            positionList -- The positions used for the builder
            mergeRule -- rules for merging identically named taxa
        static GenotypeTableBuilder getTaxaIncremental(GenotypeTable genotypeTable, GenotypeMergeRule mergeRule)
            genotypeTable -- input genotype table
            mergeRule -- rules for mergin identically named taxa
        static GenotypeTableBuilder getTaxaIncremental(PositionList positionList, String newHDF5File)
            positionList -- the defined list of positions
            newHDF5File -- hdf5 file to be created

        Returns:

        Builder to add taxa to
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableBuilder'],"mergeTaxaIncremental",
                        (make_sig([java_imports['String'],java_imports['GenotypeMergeRule']],
                                  java_imports['GenotypeTableBuilder']),(metaString, GenotypeMergeRule),
                        lambda x: GenotypeTableBuilder(obj=x)))
    def mergeTaxaIncremental(*args):
        """ Merges taxa to an existing HDF5 file.

        The position list is derived from the positions already in the
        existing HDF5 file

        Signatures:

        static GenotypeTableBuilder mergeTaxaIncremental(String existingHDF5File,
                                    GenotypeMergeRule mergeRule)

        Arguments:

        static GenotypeTableBuilder mergeTaxaIncremental(String existingHDF5File,
                                    GenotypeMergeRule mergeRule)
            existingHDF5File -- An estigin HDF5 file containing positions
            mergeRule -- rule for gergin taxa

        Returns:

        Builder to merge taxa with
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableBuilder'],'getTaxaIncrementalWithMerging',
                        (make_sig([java_imports['String'],java_imports['PositionList'],
                                   java_imports['GenotypeMergeRule']], java_imports['GenotypeTableBuilder']),
                        (metaString, PositionList, GenotypeMergeRule), lambda x: GenotypeTableBuilder(obj=x)))
    def getTaxaIncrementalWithMerging(*args):
        """ Creates a new taxa incremental HDF5 GenotypeTableBuilder to which
        replicate taxa can be added

        Signatures:

        static GenotypeTableBuilder getTaxaIncrementalWithMerging(String newHDF5File,
                              PositionList positionList, GenotypeMergeRule mergeRule)

        Arguments:

        newHDF5File -- the HDF5 file name
        positionList -- The postions used for the builder
        mergeRule -- rule for merging taxa

        Returns:

        new GenotypeTableBuilder
        """
        pass
    @javaStaticOverload(java_imports['GenotypeTableBuilder'],'getSiteIncremental',
                        (make_sig([java_imports['TaxaList']],java_imports['GenotypeTableBuilder']),
                         (TaxaList,), lambda x: GenotypeTableBuilder(obj=x)),
                         (make_sig([java_imports['TaxaList'],'int',java_imports['String']],
                                   (TaxaList, metaInteger, metaString),
                                   lambda x: GenotypeTableBuilder(obj=x))))
    def getSiteIncremental(*args):
        """ Build an alignment site by site in memory

        Signatures:

        static GenotypeTableBuilder getSiteIncremental(TaxaList taxaList)
        static GenotypeTableBuilder getSiteIncremental(TaxaList taxaList,
                                int numberOfPositions, String newHDF5File)

        Arguments:

        static GenotypeTableBuilder getSiteIncremental(TaxaList taxaList)
            taxaList -- taxa used to build to alignment
        static GenotypeTableBuilder getSiteIncremental(TaxaList taxaList,
                                int numberOfPositions, String newHDF5File)
            taxaList -- taxa used to build alignment
            numberOfPositions -- Total number of positions to be added
            newHDF5File -- HDF5 file to store the GenotypeTable data
            
        Returns:

        builder to add sites to
        """
        pass
    # TODO: Finish class
    @javaStaticOverload(java_imports['GenotypeTableBuilder'],'getInstance',
                        (make_sig([java_imports['GenotypeCallTable'], java_imports['PositionList'],
                                   java_imports['TaxaList'], java_imports['AlleleDepth'],
                                   java_imports['AlleleProbability'],java_imports['ReferenceProbability'],
                                   java_imports['Dosage'],java_imports['GeneralAnnotationStorage']],
                                   java_imports['GenotypeTable'])))
    def getInstance(*args):
        """ Standard approach for creating new Alignment. Also provides methods
        for creating HDF5 file based on existing Genotype, PostionList, TaxaList

        Signatures:

        static GenotypeTable getInstance(GenotypeCallTable genotype, PositionList positionList,
                             TaxaList taxaList, AlleleDepth alleleDepth,
                             AlleleProbability alleleProbability, Dosage dosage,
                             GeneralAnnotationStorage annotations)
        static GenotypeTable getInstance(GenotypeCallTable genotype, PositionList positionList,
                             TaxaList taxaList, AlleleDepth alleleDepth)
        static GenotypeTable getInstance(GenotypeCallTable genotype, PositionList positionList,
                             TaxaList taxaList)
        static GenotypeTable getInstance(GenotypeCallTable genotype, PositionList positionList,
                             TaxaList taxaList, String hdf5File)
        static GenotypeTable getInstance(GenotypeTable a, String hdf5File)
        static GenotypeTable getInstance(String hdf5File)

        Arguments:

        static GenotypeTable getInstance(GenotypeCallTable genotype, PositionList positionList,
                             TaxaList taxaList, AlleleDepth alleleDepth,
                             AlleleProbability alleleProbability, Dosage dosage,
                             GeneralAnnotationStorage annotations)
            genotype -- The genotype calls
            positionList -- The positions
            taxaList -- The taxa
            alleleDepth -- allele depth
            alleleProbability -- allele probability
            dosage -- Dosage
            annotations -- annotations
        static GenotypeTable getInstance(GenotypeCallTable genotype, PositionList positionList,
                             TaxaList taxaList, AlleleDepth alleleDepth)
            genotype -- The genotype calls
            positionList -- The positions
            taxaList -- the taxa
            alleleDepth -- the allele depth
        static GenotypeTable getInstance(GenotypeCallTable genotype, PositionList positionList,
                             TaxaList taxaList)
            genotype -- The genotype calls
            positionList -- The positions
            taxaList -- the taxa
        static GenotypeTable getInstance(GenotypeCallTable genotype, PositionList positionList,
                             TaxaList taxaList, String hdf5File)
            genotype -- The genotype calls
            positionList -- The positions
            taxaList -- the taxa
            hdf5File -- Name of the file containing existing Genotype, PositionList, TaxaList
        static GenotypeTable getInstance(GenotypeTable a, String hdf5File)
            a -- Existing alignment
            hdf5File -- name of the file to put in the alignment into
        static GenotypeTable getInstance(String hdf5File)
            hdf5File -- File containig alignment
        """
        pass
