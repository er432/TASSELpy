from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.net.maizegenetics.taxa.distance.DistanceMatrix import DistanceMatrix
from TASSELpy.net.maizegenetics.dna.snp.GenotypeTable import GenotypeTable
from TASSELpy.net.maizegenetics.trait.SimplePhenotype import SimplePhenotype
from TASSELpy.java.lang.Enum import enum as java_enum
from TASSELpy.java.lang.Enum import Enum

java_imports = {'DistanceMatrix':'net/maizegenetics/taxa/distance/DistanceMatrix',
                'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
                'Kinship':'net/maizegenetics/analysis/distance/Kinship',
                'SimplePhenotype':'net/maizegenetics/trait/SimplePhenotype'}
class Kinship(DistanceMatrix):
    """
    Kinship tools by Zhiwu Zhang
    """
    _java_name = java_imports['Kinship']
    ## Creates a kinship matrix
    @javaConstructorOverload(java_imports['Kinship'],
            (make_sig([java_imports['GenotypeTable']],'void'),(GenotypeTable,)),
            (make_sig([java_imports['SimplePhenotype']],'void'),(SimplePhenotype,)),
            (make_sig([java_imports['DistanceMatrix']],'void'),(DistanceMatrix,)))
    def __init__(self, *args, **kwargs):
        """
        Creates a kinship matrix

        Signatures:

        Kinship(GenotypeTable mar)
        Kinship(SimplePhenotype ped)
        Kinship(DistanceMatrix dm)

        Arguments:

        Kinship(GenotypeTable mar)
            mar -- A GenotypeTable used to calculated Kinship
        Kinship(SimplePhenotype ped)
            ped -- A SimplePhenotype table for calculating from Phenotype
        Kinship(DistanceMatrix dm)
            dm -- A DistanceMatrix instance
        """
        pass
    ## Gets the DistanceMatrix containing the kinship values
    # @return DistanceMatrix containing the kinship values
    @javaOverload("getDm",
                  (make_sig([],java_imports['DistanceMatrix']),(),
                   lambda x: DistanceMatrix(obj=x)))
    def getDm(self, *args):
        """
        Gets the DistanceMatrix containing the Kinship values

        Signatures:

        DistanceMatrix getDm()

        Returns:

        DistanceMatrix containing kinship values
        """
        pass
