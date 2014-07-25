from TASSELpy.java.lang.Comparable import Comparable
from TASSELpy.net.maizegenetics.util.GeneralAnnotation import GeneralAnnotation
from TASSELpy.utils.Overloading import javaOverload,javaConstructorOverload
from TASSELpy.java.lang.String import metaString
from TASSELpy.utils.helper import make_sig

java_imports = {'String':'java/lang/String',
                'Taxon':'net/maizegenetics/taxa/Taxon'}
class Taxon(Comparable, GeneralAnnotation):
    _java_name = java_imports['Taxon']
    def __repr__(self):
        return "Taxon(%s)" % self.getName()
    @javaConstructorOverload(java_imports['Taxon'],
            (make_sig([java_imports['String']],'void'),(metaString,)))
    def __init__(self, *args, **kwargs):
        """
        Instantiates a Taxon

        Signatures:

        Taxon(String name)
        """
        super(Taxon, self).__init__(*args,generic=(Taxon,),**kwargs)
    @javaOverload("toStringWithVCFAnnotation",
                  (make_sig([],java_imports['String']),(),None))
    def toStringWithVCFAnnotation(self, *args):
        """
        Signatures:

        String toStringWithVCFAnnotation()
        """
        pass
    @javaOverload("getName",
                  (make_sig([],java_imports['String']),(),None))
    def getName(self, *args):
        """
        Signatures:

        String getName()
        """
        pass
        
