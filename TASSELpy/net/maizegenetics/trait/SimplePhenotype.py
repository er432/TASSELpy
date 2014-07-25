from TASSELpy.java.lang.Object import Object
from TASSELpy.java.util.List import List
from TASSELpy.net.maizegenetics.taxa.TaxaList import TaxaList
from TASSELpy.net.maizegenetics.trait.Trait import Trait
from TASSELpy.net.maizegenetics.trait.AbstractPhenotype import AbstractPhenotype
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.utils.primativeArray import javaPrimativeArray
from TASSELpy.javaObj import javaArray
from TASSELpy.utils.helper import make_sig

java_imports = {'DoubleMatrix2D':'cern/colt/matrix/DoubleMatrix2D',
                'List':'java/util/List',
                'Phenotype':'net/maizegenetics/trait/Phenotype',
                'SimplePhenotype':'net/maizegenetics/trait/SimplePhenotype',
                'Taxon':'net/maizegenetics/taxa/Taxon',
                'TaxaList':'net/maizegenetics/taxa/TaxaList',
                'Trait':'net/maizegenetics/trait/Trait'}

class SimplePhenotype(AbstractPhenotype):
    _java_name = java_imports['SimplePhenotype']
    @javaConstructorOverload(java_imports['SimplePhenotype'],
            (make_sig([java_imports['TaxaList'],java_imports['List'],java_imports['DoubleMatrix2D']],
                      'void'), (TaxaList,List,Object)),
            (make_sig([java_imports['TaxaList'],java_imports['List'],'double[][]'],
                      'void'), (TaxaList,List,
                                javaArray.get_array_type(javaPrimativeArray.get_array_type('double')))),
            (make_sig([java_imports['TaxaList'],java_imports['List']],'void'),
             (TaxaList,List)))
    def __init__(self, *args, **kwargs):
        """
        Instantiates a SimplePhenotype object

        Signatures:

        SimplePhenotype(TaxaList taxa, List<Trait> traits, DoubleMatrix2D data)
        SimplePhenotype(TaxaList taxa, List<Trait> traits, double[][] data)
        SimplePhenotype(TaxaList taxa, List<Trait> traits)
        """
        pass
