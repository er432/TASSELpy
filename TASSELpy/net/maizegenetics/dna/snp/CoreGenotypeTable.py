from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload
import javabridge

## Dictionary to hold java imports
java_imports = {'AlleleDepth':'net/maizegenetics/dna/snp/depth/AlleleDepth',
                'BitSet':'net/maizegenetics/util/BitSet',
                'Chromosome':'net/maizegenetics/dna/map/Chromosome',
                'CoreGenotypeTable':'net/maizegenetics/dna/snp/CoreGenotypeTable',
                'GenotypeTable':'net.maizegenetics.dna.snp.GenotypeTable',
                'GenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/GenotypeCallTable',
                'PositionList':'net/maizegenetics/dna/map/PositionList',
                'SiteScore':'net/maizegenetics/dna/snp/score/SiteScore',
                'TaxaList':'net/maizegenetics/taxa/TaxaList'}

class CoreGenotypeTable(GenotypeTable):
    _java_name = java_imports['CoreGenotypeTable']
    @javaConstructorOverload(java_imports['CoreGenotypeTable'],
                (make_sig([java_imports['GenotypeCallTable'],java_imports['PositionList'],
                           java_imports['TaxaList']],'void'),(object,object,object)),
                (make_sig([java_imports['GenotypeCallTable'],java_imports['PositionList'],
                           java_imports['TaxaList'],java_imports['SiteScore'],
                           java_imports['AlleleDepth']],'void'),(object,object,object,object,object)))
    def __init__(self,*args,**kwargs):
        """
        Instantiates a CoreGenotypeTable

        Signatures:

        CoreGenotypeTable(GenotypeCallTable genotype, PositionList positionList,
             TaxaList taxaList, SiteScore siteScore, AlleleDepth alleleDepth)
        CoreGenotypeTable(GenotypeCallTable genotype, PositionList positionList, TaxaList taxaList)
        """
        pass

