from TASSELpy.net.maizegenetics.plugindef.AbstractPlugin import AbstractPlugin
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Boolean import metaBoolean

java_imports = {'UnionAlignmentPlugin':'net/maizegenetics/analysis/data/UnionAlignmentPlugin',
                'Frame':'java/awt/Frame'}
class UnionAlignmentPlugin(AbstractPlugin):
    _java_name = java_imports['UnionAlignmentPlugin']
    @javaConstructorOverload(java_imports['UnionAlignmentPlugin'],
                             (make_sig([java_imports['Frame'],'boolean'],'void'),
                              (Object,metaBoolean)))
    def __init__(self, *args, **kwargs):
        """ Creates a new instance of UnionAlignmentPlugin

        Signatures:

        UnionAlignmentPlugin(Frame parentFrame, boolean isInteractive)

        Arguments:

        parentFrame -- A frame, can be null
        isInteractive -- Whether in an interactive session
        """
        pass
