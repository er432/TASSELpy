from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload, javaStaticOverload
from TASSELpy.net.maizegenetics.util.GeneralAnnotation import GeneralAnnotation
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.String import metaString
from TASSELpy.java.lang.Number import metaNumber

java_imports = {'GeneralAnnotationStorage':'net/maizegenetics/util/GeneralAnnotationStorage',
                'Number':'java/lang/Number',
                'String':'java/lang/String'}

class GeneralAnnotationStorage(GeneralAnnotation):
    """ Stores general annotations
    """
    _java_name = java_imports['GeneralAnnotationStorage']
    @javaStaticOverload(java_imports['GeneralAnnotationStorage'],"getBuilder",
                        (make_sig([],java_imports['GeneralAnnotationStorage']+'$Builder'),
                         (),lambda x: GeneralAnnotationStorage.Builder(obj=x)))
    def getBuilder(self, *args):
        """ Gets a builder for a GeneralAnnotationStorage object

        Signatures:

        static Builder getBuilder()

        Returns:

        A builder
        """
        pass
    # Future: put in HDF5 read/write utils
    class Builder(Object):
        """ Builder for GeneralAnnotationStorage
        """
        _java_name = java_imports['GeneralAnnotationStorage']+'$Builder'
        @javaConstructorOverload(java_imports['GeneralAnnotationStorage']+'$Builder')
        def __init__(self, *args, **kwargs):
            pass
        @javaOverload("addAnnotation",
                      (make_sig([java_imports['String'],java_imports['String']],
                                java_imports['GeneralAnnotationStorage']+'$Builder'),
                       (metaString, metaString), lambda x: Builder(obj=x)),
                       (make_sig([java_imports['String'],java_imports['Number']],
                                 java_imports['GeneralAnnotationStorage']+'$Builder'),
                        (metaString, metaNumber), lambda x: Builder(obj=x)))
        def addAnnotation(self, *args):
            """ Add a non-standard annotation

            Signatures:

            Builder addAnnotation(String key, String value)
            Builder addAnnotation(String key, Number value)

            Arguments:

            Builder addAnnotation(String key, String value)
                key -- key
                value -- value
            Builder addAnnotation(String key, Number value)
                key -- key
                value -- value

            Returns:

            Instance of the builder with the annotation added
            """
            pass
        @javaOverload("build",
                      (make_sig([],java_imports['GeneralAnnotationStorage']),(),
                       lambda x: GeneralAnnotationStorage(obj=x)))
        def build(self, *args):
            """ Builds the GeneralAnnotationStorage object

            Signatures:

            GeneralAnnotationStorage build()

            Returns:

            The built object
            """
            pass
        
        
