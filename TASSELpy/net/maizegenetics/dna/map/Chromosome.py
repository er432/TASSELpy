from TASSELpy.net.maizegenetics.util.GeneralAnnotation import GeneralAnnotation
from TASSELpy.java.lang.Comparable import Comparable
from TASSELpy.utils.helper import make_sig
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.String import metaString
from TASSELpy.utils.Overloading import javaConstructorOverload,javaStaticOverload,javaOverload

java_imports = {'Chromosome':'net/maizegenetics/dna/map/Chromosome',
                'GeneralAnnotation':'net/maizegenetics/util/GeneralAnnotation',
                'String':'java/lang/String'}

## Class only used to refer to Chromosome type within Chromosome body
class MetaChromosome(Comparable, GeneralAnnotation):
    pass

## Defines the chromosome structure and length. The name and length
# recroded for each chromosome
class Chromosome(MetaChromosome):
    """
    Defines the chromosome structure and length. The name and length
    recorded for each chromosome
    """
    _java_name = java_imports['Chromosome']
    ## Instantiates a Chromosome object
    # @param name Name of the chromosome
    # @param length Length of chromosome in base pairs
    # @param features Map of features about the chromosome
    @javaConstructorOverload(java_imports['Chromosome'],
                (make_sig([java_imports['String'],'int',java_imports['GeneralAnnotation']],
                          'void'),(metaString,metaInteger,GeneralAnnotation)),
                (make_sig([java_imports['String']],'void'),(metaString,)))
    def __init__(self, *args, **kwargs):
        """
        Instantiates a Chromosome object

        Signatures:

        Chromosome(String name, int length, GeneralAnnotation features)
        Chromosome(String name)

        Arguments:

        Chromosome(String name, int length, GeneralAnnotation features)
           name -- Name of the chromosome
           length -- Length of chromosome in base pairs
           features -- Map of features about the chromosome
        Chromosome(String name)
           name -- Name of the chromosome
        """
        pass
    @javaStaticOverload(java_imports['Chromosome'],"getCanonicalChromosome",
            (make_sig([java_imports['Chromosome']],java_imports['Chromosome']),
             (MetaChromosome,),lambda x: Chromosome(obj=x)))
    def getCanonicalChromosome(*args):
        """

        Signatures:

        static Chromosome getCanonicalChromosome(Chromosome chr)
        """
        pass
    ## Gets the name of the chromosome
    # @return The name of the chromosome
    @javaOverload("getName",
                  (make_sig([],java_imports['String']),(),None))
    def getName(self, *args):
        """
        Gets the name of the chromosome

        Signatures:

        String getName()

        Returns:

        The name of the chromosome
        """
        pass
    ## Returns the integer value of the chromosome (if name is not a number
    # then Integer.MAX_VALUE is returned
    # @return The integer value of the chromosome
    @javaOverload("getChromosomeNumber",
                  (make_sig([],'int'),(),None))
    def getChromosomeNumber(self, *args):
        """
        Returns the integer value of the chromosome (if name is not a number
        then Integer.MAX_VALUE is returned

        Signatures:

        int getChromosomeNumber()

        Returns:

        The integer value of the chromosome
        """
        pass
    ## Gets the length of the chromosome in base pairs
    # @return The length of the chromosome in base pairs
    @javaOverload("getLength",
                  (make_sig([],'int'),(),None))
    def getLength(self, *args):
        """
        Gets the length of the chromosome in base pairs

        Signatures:

        int getLength()

        Returns:

        The length of the chromosome in base pairs
        """
        pass
