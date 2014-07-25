from TASSELpy.utils.Overloading import javaOverload
from TASSELpy.utils.helper import make_sig
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.String import String
import javabridge

java_imports = {'Map':'java/util/Map',
                'GeneralAnnotation':'net/maizegenetics/util/GeneralAnnotation',
                'Object':'java/lang/Object',
                'SetMultimap':'com/google/common/collect/SetMultimap',
                'String':'java/lang/String'}

## Provide generalized annotations (descriptors) for taxon or site
class GeneralAnnotation(Object):
    """
    Provide generalized annotations (descriptors) for taxon or site
    """
    _java_name = java_imports['GeneralAnnotation']
    ## Returns all annotation values for a given annotation key
    # @param annoName annotation key
    # @return array of annotation values (if not present new String[0])
    @javaOverload("getAnnotation",
                  (make_sig([java_imports['String']],java_imports['Object']+'[]'),
                   (str,),lambda x: javabridge.get_env().get_object_array_elements(x)))
    def getAnnotation(self, *args):
        """
        Returns all annotation value for a given annotation key

        Signatures:

        Object[] getAnnotation(String annoName)

        Arguments:

        annoName -- annotation key

        Returns:

        array of annotation values (if not present new String[0])
        """
        pass
    ## Returns all annotation values for a given annotation key
    # @param annoName annotation key
    # @return array of annotation values (if not present new String[0])
    @javaOverload("getTextAnnotation",
                  (make_sig([java_imports['String']],java_imports['String']+'[]'),(str,),
                   lambda x: map(lambda y: String(obj=y).toString(),
                                 javabridge.get_env().get_object_array_elements(x))))
    def getTextAnnotation(self, *args):
        """
        Returns all annotation values for a given annotation key

        Signatures:

        String[] getTextAnnotation(String annoName)

        Arguments:

        annoName -- annotation key

        Returns:

        array of annotation values (if not present new String[0])
        """
        pass
    ## Returns consensus value for given annotation key
    # @param annoName annotation key
    # @return Consensus value (if not present new String[0])
    @javaOverload("getConsensusAnnotation",
                  (make_sig([java_imports['String']],java_imports['String']),(str,),
                   None))
    def getConsensusAnnotation(self, *args):
        """
        Returns consensus value for given annotation key

        Signatures:

        String getConsensusAnnotation(String annoName)

        Arguments:

        annoName -- annotation key

        Returns:

        Consensus value (if not present new String[0])
        """
        pass
    ## Returns all annotation value for given annotation key
    # @param annoName annotation key
    # @return array of annotation values (if not present new double[0])
    @javaOverload("getQuantAnnotation",
                  (make_sig([java_imports['String']],'double[]'),(str,),
                   lambda x: javabridge.get_env().get_double_array_elements(x)))
    def getQuantAnnotation(self, *args):
        """
        Returns all annotation value for given annotation key

        Signatures:

        double[] getQuantAnnotation(String annoName)

        Arguments:

        annoName -- annotation key

        Returns:

        array of annotation values (if not present new double[0])
        """
        pass
    ## Returns average annotation for a given annotation key
    # @param annoName annotation key
    # @return average value (if not present - return Double.NaN)
    @javaOverload("getAverageAnnotation",
                  (make_sig([java_imports['String']],'double'),(str,),None))
    def getAverageAnnotation(self, *args):
        """
        Returns average annotation for a given annotation key

        Signatures:

        double getAverageAnnotation(String annoName)

        Arguments:

        annoName -- annotation key

        Returns:

        average value (if not present - return Double.NaN)
        """
        pass
    ## Returns all annotation Map.Entries
    # @return Array of Map.Entry
    @javaOverload("getAllAnnotationEntries",
                  (make_sig([],java_imports['Map']+'$Entry[]'),(),
                   lambda x: javabridge.get_env().get_object_array_elements(x)))
    def getAllAnnotationEntries(self, *args):
        """
        Returns all annotation Map.Entries

        Signatures:

        Map.Entry<String, String>[] getAllAnnotationEntries()

        Returns:

        Array of Map.Entry
        """
        pass
    ## Returns all annotations in TreeMap
    # @return Map of annotations
    @javaOverload("getAnnotationAsMap",
                  (make_sig([],java_imports['SetMultimap']),(),
                   None))
    def getAnnotationAsMap(self, *args):
        """
        Returns all annotations in TreeMap

        Signatures:

        SetMultimap<String,String> getAnnotationAsMap()

        Returns:

        Map of annotations
        """
        pass
