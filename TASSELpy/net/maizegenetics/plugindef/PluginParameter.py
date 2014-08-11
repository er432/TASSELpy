from TASSELpy.utils.Overloading import javaConstructorOverload
from TASSELpy.java.lang.Comparable import Comparable
from TASSELpy.java.lang.Object import Object
from TASSELpy.javaObj import genericJavaObj

class PluginParameter(genericJavaObj, Object):
    """ Defines the attributes of parameters to be used in the plugins
    """
    def __init__(self, *args, **kwargs):
        super(PluginParameter, self).__init__(*args, **kwargs)
    # TODO: finish class
