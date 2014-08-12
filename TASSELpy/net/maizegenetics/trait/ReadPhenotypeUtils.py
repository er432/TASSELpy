from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload, javaStaticOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.String import String, metaString
from TASSELpy.utils.primativeArray import meta_double_array
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.javaObj import javaArray
from TASSELpy.net.maizegenetics.trait.Trait import Trait
from TASSELpy.net.maizegenetics.trait.Phenotype import Phenotype

java_imports = {'Phenotype':'net/maizegenetics/trait/Phenotype',
                'ReadPhenotypeUtils':'net/maizegenetics/trait/ReadPhenotypeUtils',
                'String':'java/lang/String',
                'Trait':'net/maizegenetics/trait/Trait'}

class ReadPhenotypeUtils(Object):
    _java_name = java_imports['ReadPhenotypeUtils']
    @javaConstructorOverload(java_imports['ReadPhenotypeUtils'])
    def __init__(self, *args, **kwargs):
        pass
    @javaStaticOverload(java_imports['ReadPhenotypeUtils'], "makeCharacterTrait",
                        (make_sig([java_imports['String']+'[]','double[]',
                                   java_imports['String'],java_imports['String']],
                                   java_imports['Trait']),(javaArray.get_array_type(String),
                                                           meta_double_array, metaString,
                                                           metaString), lambda x: Trait(obj=x)))
    def makeCharacterTrait(*args):
        """ Makes a character trait

        Signatures:

        static Trait makeCharacterTrait(String[] original, double[] tonumber,
                                        String name, String type)

        Arguments:

        original -- the original class or discrete data
        tonumber -- a double array, the same length as the original data, which
                    will hold the class indices
        name -- the trait name
        type -- the trait type

        Returns:

        The new trait
        """
        pass
    @javaStaticOverload(java_imports["ReadPhenotypeUtils"], "doubleFromCharacterTrait",
                        (make_sig([java_imports['Trait'], java_imports['String']+'[]'],
                                 'double[]'), (Trait, javaArray.get_array_type(String)),
                                 lambda x: javaPrimativeArray.make_array_from_obj('double',x)))
    def doubleFromCharacterTrait(*args):
        """ Converts a character trait to doubles

        Signatures:

        static double[] doubleFromCharacterTrait(Trait trait, String[] textdata)

        Arguments:

        trait -- trait
        textdata -- the current data

        Returns:

        The new trait
        """
        pass
    @javaStaticOverload(java_imports["ReadPhenotypeUtils"], "readPolymorphismAlignment",
                        (make_sig([java_imports['String']], java_imports['Phenotype']),
                         (metaString,), lambda x: Phenotype(obj=x)))
    def readPolymorphismAlignment(*args):
        """ Reads the polymorphism data from a TASSEL v2 polymorphism format file

        Signatures:

        static Phenotype readPolymorphismAlignment(String inputFile) throws IOException

        Arguments:

        inputFile -- The input file in TASSEL v2 polymorphism format

        Returns:

        a Phenotype
        """
        pass
    @javaStaticOverload(java_imports['ReadPhenotypeUtils'],'readNumericalAlignment',
                        (make_sig([java_imports['String']], java_imports['Phenotype']),
                         (metaString,), lambda x: Phenotype(obj=x)))
    def readNumericalAlignment(*args):
        """ Reads Phenotype from a file in TASSEL v2 numerical format

        Signatures:

        static Phenotype readNumericalAlignment(String inputFile) throws IOException

        Arguments:

        inputFile -- the input file in TASSEL v2 numerical format

        Returns:

        a Phenotype
        """
        pass
    @javaStaticOverload(java_imports['ReadPhenotypeUtils'],'readGenericFile',
                        (make_sig([java_imports['String']], java_imports['Phenotype']),
                         (metaString,), lambda x: Phenotype(obj=x)))
    def readGenericFile(*args):
        """ Reads input file with TASSEL v3 annotations or with no input directive

        Signatures:

        static Phenotype readGenericFile(String inputFile) throws IOException

        Arguments:

        inputFile -- the input file with TASSEL v3 annotations or with no input directives

        Returns:

        a Phenotype
        """
        pass
