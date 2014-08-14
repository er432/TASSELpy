from TASSELpy.net.maizegenetics.plugindef.AbstractPlugin import AbstractPlugin
from TASSELpy.net.maizegenetics.analysis.data.UnionAlignmentPlugin import UnionAlignmentPlugin
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Boolean import metaBoolean

java_imports = {'IntersectionAlignmentPlugin':'net/maizegenetics/analysis/data/IntersectionAlignmentPlugin',
                'Frame':'java/awt/Frame'}
class IntersectionAlignmentPlugin(UnionAlignmentPlugin):
    _java_name = java_imports['IntersectionAlignmentPlugin']
    @javaConstructorOverload(java_imports['IntersectionAlignmentPlugin'],
                             (make_sig([java_imports['Frame'],'boolean'],'void'),
                              (Object,metaBoolean)))
    def __init__(self, *args, **kwargs):
        """ Creates a new instance of IntersectionAlignmentPlugin

        Signatures:

        IntersectionAlignmentPlugin(Frame parentFrame, boolean isInteractive)

        Arguments:

        parentFrame -- A frame, can be null
        isInteractive -- Whether in an interactive session
        """
        pass
