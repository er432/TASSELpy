from TASSELpy.net.maizegenetics.dna.snp.genotypecall.GenotypeCallTable import GenotypeCallTable
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.String import String
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.javaObj import javaArray
import javabridge
import numpy as np


# Dictionary to hold java objects
java_imports = {'GenotypeTable':'net/maizegenetics/dna/snp/GenotypeTable',
		'GenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/GenotypeCallTable',
		'AbstractGenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/AbstractGenotypeCallTable',
                'String':'java/lang/String'
                }


class AbstractGenotypeCallTable(GenotypeCallTable):
    """ Abstract implementation of methods in GenotypeCallTable
    """
    _java_name = java_imports['AbstractGenotypeCallTable']
    @javaConstructorOverload(java_imports['AbstractGenotypeCallTable'],
                             (make_sig(['int','int','boolean',java_imports['String']+'[][]',
                                        'int'],'void'),(metaInteger, metaInteger, metaBoolean,
                                                 javaArray.get_array_type(javaArray.get_array_type(String)),
                                                        metaInteger)),
                             (make_sig(['int','int','boolean',java_imports['String']+'[][]'],
                                       'void'),(metaInteger,metaInteger,metaBoolean,
                                                javaArray.get_array_type(javaArray.get_array_type(String)))))
    def __init__(self, *args, **kwargs):
        """ Abstract constructor for GenotypeCallTable

        Signatures:

        AbstractGenotypeCallTable(int numTaxa, int numSites, boolean phased,
                                  String[][] alleleEncodings, int maxNumAlleles)
        AbstractGenotypeCallTable(int numTaxa, int numSites, boolean phased,
                                  String[][] alleleEncodings)
        """
        pass

