from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.String import metaString
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload
from TASSELpy.java.lang.Class import Class

java_imports = {'Class':'java/lang/Class',
                'Datum':'net/maizegenetics/plugindef/Datum',
                'Object':'java/lang/Object',
                'String':'java/lang/String'}

class Datum(Object):
    """ This wraps data elements used as input or output to TASSEL
    modules
    """
    _java_name = java_imports['Datum']
    @javaConstructorOverload(java_imports['Datum'],
                             (make_sig([java_imports['String'], java_imports['Object'],
                                        java_imports['String']],'void'),(metaString, Object,
                                                                         metaString)))
    def __init__(self, *args, **kwargs):
        """ Creats a new instance of Datum

        Signatures:

        Datum(String name, Object data, String comment)

        Arguments:

        name -- name of this data instance
        data -- data element
        comment -- optional comment
        """
        pass
    @javaOverload("getName",
                  (make_sig([],java_imports['String']), (), None))
    def getName(self, *args):
        """ Gets the name of the datum

        Signatures:

        String getName()

        Returns:

        The name of the datum
        """
        pass
    @javaOverload("setName",
                  (make_sig([java_imports['String']],'void'),(),None))
    def setName(self, *args):
        """ Sets the name of the datum

        Signatures:

        void setName(String s)

        Arguments:

        s -- The name to give to the datum
        """
        pass
    @javaOverload("getData",
                  (make_sig([],java_imports['Object']),(),lambda x: Object(obj=x)))
    def getData(self, *args):
        """ Gets the data

        Signatures:

        Object getData()

        Returns:

        The data
        """
        pass
    @javaOverload("getComment",
                  (make_sig([], java_imports['String']),(),None))
    def getComment(self, *args):
        """ Gets the comment for the datum

        Signatures:

        String getComment()

        Returns:

        The comment for the datum
        """
        pass
    @javaOverload("getDataType",
                  (make_sig([],java_imports['Class']),(),
                   lambda x: Class(obj=x)))
    def getDataType(self, *args):
        """ Gets the class of the datum

        Signatures:

        Class getDataType()

        Returns:

        The Class of the Data
        """
        pass
