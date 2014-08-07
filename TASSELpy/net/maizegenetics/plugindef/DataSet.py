from TASSELpy.java.lang.Object import Object
from TASSELpy.java.util.List import List
from TASSELpy.net.maizegenetics.plugindef.Datum import Datum
from TASSELpy.utils.helper import make_sig
from TASSELpy.javaObj import javaArray
from TASSELpy.utils.Overloading import javaConstructorOverload, javaConstructorOverload
import TASSELpy.net.maizegenetics.plugindef.Plugin

## Dictionary to hold java imports
java_imports = {'DataSet':'net/maizegenetics/plugindef/DataSet',
                'Datum':'net/maizegenetics/plugindef/Datum',
                'List':'java/util/List',
                'Plugin':'net/maizegenetics/plugindef/Plugin'}

class DataSet(Object):
    """ This is a set of Datum """
    _java_name = java_imports['DataSet']
    @javaConstructorOverload(java_imports['DataSet'],
                             (make_sig([java_imports['List'],java_imports['Plugin']],'void'),
                               (List, TASSELpy.net.maizegenetics.plugindef.Plugin.Plugin)),
                             (make_sig([java_imports['Datum'],java_imports['Plugin']],'void'),
                               (Datum, TASSELpy.net.maizegenetics.plugindef.Plugin.Plugin)),
                             (make_sig([java_imports['Datum']+'[]',java_imports['Plugin']],'void'),
                               javaArray.get_array_type(Datum)))
    def __init__(self, *args, **kwargs):
        """
        Instantiates a DataSet

        Signatures:

        DataSet(List<Datum> list, Plugin creator)
        DataSet(Datum theDatum, Plugin creator)
        DataSet(Datum[] list, Plugin creator)

        Arguments:

        DataSet(List<Datum> list, Plugin creator)
            list -- list of data elements
            creator -- creating plugin
        DataSet(Datum theDatum, Plugin creator)
            theDatum -- a single Datum
            creator -- creating plugin
        DataSet(Datum[] list, Plugin creator)
            list -- list of data elements
            creator -- creating plugin
        """
        pass
    # TODO: Finish class
