from TASSELpy.java.util.List import List
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload, javaGenericOverload
from TASSELpy.net.maizegenetics.plugindef.Plugin import Plugin

java_imports = {'AbstractPlugin':'net/maizegenetics/plugindef/AbstractPlugin',
                'List':'java/util/List',
                'Plugin':'net/maizegenetics/plugindef/Plugin'}
class AbstractPlugin(Plugin):
    _java_name = java_imports['AbstractPlugin']
    @javaConstructorOverload("AbstractPlugin",
                             (make_sig([],'void'),()))
    def __init__(self, *args, **kwargs):
        """ Creates a new instance of AbstractPlugin

        Signatures:

        AbstractPlugin()
        """
        pass
    @javaGenericOverload("getInputs",
                  (make_sig([],java_imports['List']),(),
                   dict(type=List, generic=(Plugin,))))
    def getInputs(self, *args):
        """ Gets list of inputs

        Signatures:

        List<Plugin> getInputs()

        Returns:

        List of inputs
        """
        pass
