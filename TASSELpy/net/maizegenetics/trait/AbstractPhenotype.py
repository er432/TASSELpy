from TASSELpy.net.maizegenetics.trait.Phenotype import Phenotype
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.utils.helper import make_sig

java_imports = {'Phenotype':'net/maizegenetics/trait/Phenotype',
                'AbstractPhenotype':'net/maizegenetics/trait/AbstractPhenotype'}
class AbstractPhenotype(Phenotype):
    @javaConstructorOverload(java_imports['AbstractPhenotype'])
    def __init__(self, *args, **kwargs):
        pass
