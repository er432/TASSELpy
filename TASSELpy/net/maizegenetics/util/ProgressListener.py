from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.utils.Overloading import javaConstructorOverload,javaOverload
from TASSELpy.utils.helper import make_sig

java_imports = {'Object':'java/lang/Object',
                'ProgressListener':'net/maizegenetics/util/ProgressListener'}
class ProgressListener(Object):
    _java_name = java_imports['ProgressListener']
    @javaConstructorOverload(java_imports['ProgressListener'])
    def __init__(self, *args, **kwargs):
        pass
    ## Returns the progress of execution
    # @param percent percent complete
    # @param meta meta data
    @javaOverload("progress",
                (make_sig(['int',java_imports['Object']],'void'),(metaInteger,Object),None))
    def progress(self, *args):
        """
        Returns the progress of execution

        Signatures:

        void progress(int percent, Object meta)

        Arguments:

        percent -- percent complete
        meta -- meta data
        """
        pass
