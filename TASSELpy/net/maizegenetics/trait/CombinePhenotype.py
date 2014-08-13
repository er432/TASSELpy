from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload, javaStaticOverload
from TASSELpy.net.maizegenetics.trait.AbstractPhenotype import AbstractPhenotype
from TASSELpy.net.maizegenetics.trait.Phenotype import Phenotype
from TASSELpy.net.maizegenetics.trait.SimplePhenotype import SimplePhenotype
from TASSELpy.net.maizegenetics.trait import Trait
from TASSELpy.net.maizegenetics.taxa.Taxon import Taxon
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Double import metaDouble
from TASSELpy.javaObj import javaArray

java_imports = {'CombinePhenotype': 'net/maizegenetics/trait/CombinePhenotype',
                'Phenotype':'net/maizegenetics/trait/Phenotype',
                'SimplePhenotype':'net/maizegenetics/trait/SimplePhenotype',
                'Taxon':'net/maizegenetics/taxa/Taxon',
                'Trait':'net/maizegenetics/trait/Trait'}

class CombinePhenotype(AbstractPhenotype):
    """ Class used for combining multiple phenotypes that may have different taxa
    among them
    """
    _java_name = java_imports['CombinePhenotype']
    @javaConstructorOverload(java_imports['CombinePhenotype'])
    def __init__(self, *args, **kwargs):
        pass
    @javaStaticOverload(java_imports['CombinePhenotype'],"getInstance",
                        (make_sig([java_imports['Phenotype'],java_imports['Phenotype'],'boolean'],
                                  java_imports['CombinePhenotype']),
                         (Phenotype,Phenotype,metaBoolean),
                         lambda x: CombinePhenotype(obj=x)),
                         (make_sig([java_imports['Phenotype']+'[]','boolean'],
                                   java_imports['CombinePhenotype']),
                          (javaArray.get_array_type(Phenotype),metaBoolean),
                          lambda x: CombinePhenotype(obj=x)))
    def getInstance(*args):
        """ Gets an instance of CombinePhenotype, allowing combining of more than
        one phenotype

        Signatures:

        static CombinePhenotype getInstance(Phenotype phenotype1, Phenotype phenotype2,
                                boolean isUnion)
        static CombinePhenotype getInstance(Phenotype[] phenotypes, boolean isUnion)

        Arguments:

        static CombinePhenotype getInstance(Phenotype phenotype1, Phenotype phenotype2,
                                boolean isUnion)
            phenotype1 -- The first phenotype
            phenotype2 -- The second phenotype
            isUnion -- Whether to take the union of the taxa. If false, takes the intersection
        static CombinePhenotype getInstance(Phenotype[] phenotypes, boolean isUnion)
            phenotypes -- List of Phenotype objects to combine
            isUnion -- Whether to take the union of the taxa in the Phenotypes. If false,
                       takes the intersection
        """
        pass
    @javaOverload("setData",
                  (make_sig([java_imports['Taxon'],java_imports['Trait'],'double'],'void'),
                   (Taxon,Trait,metaDouble),None),
                   (make_sig(['int','int','double'],'void'),
                    (metaInteger,metaInteger,metaDouble),None))
    def setData(self, *args):
        """ Sets a particular data value

        Signatures:

        void setData(Taxon taxon, Trait trait, double value)
        void setData(int taxon, int trait, double value)

        Arguments:

        void setData(Taxon taxon, Trait trait, double value)
            taxon -- A Taxon instance
            trait -- A Trait instance
            value -- The value to set
        void setData(int taxon, int trait, double value)
            taxon -- index of a taxon
            trait -- index of a trait
            value -- The value to set
        """
        pass
    @javaOverload("simpleCopy",
                  (make_sig([],java_imports['SimplePhenotype']),(),
                   lambda x: SimplePhenotype(obj=x)))
    def simpleCopy(self, *args):
        """ Makes a copy of the CombinePhenotype as a SimplePhenotype

        Signatures:

        SimplePhenotype simpleCopy()

        Returns:

        A SimplePhenotype copy of the object
        """
        pass
