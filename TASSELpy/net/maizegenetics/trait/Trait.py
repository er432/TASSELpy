from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Comparable import Comparable
from TASSELpy.java.lang.String import String, metaString
from TASSELpy.java.lang.Boolean import metaBoolean
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.util.ArrayList import ArrayList
from TASSELpy.java.util.Map import Map
from TASSELpy.java.util.Set import Set
from TASSELpy.javaObj import javaArray
from TASSELpy.utils.helper import make_sig, send_to_java
from TASSELpy.utils.Overloading import javaOverload, javaConstructorOverload, javaStaticOverload
from TASSELpy.utils.Overloading import javaGenericOverload
from abc import ABCMeta

java_imports = {'ArrayList':'java/util/ArrayList',
                'Map':'java/util/Map',
                'Object':'java/lang/Object',
                'Set':'java/util/Set',
                'String':'java/lang/String',
                'Trait':'net/maizegenetics/trait/Trait'}

class metaTrait:
    __metaclass__ = ABCMeta
    @classmethod
    def __subclasshook__(cls, C):
        if issubclass(C, Trait):
            return True
        else:
            return False

class Trait(Comparable):
    """
    Data descriptor that contains information about a trait, factor, covariate, 
    or other item for which data may be stored. It may contain information 
    about the experimental unit on which data was collected (factors). It may contain information 
    about how the data is to be used in an analysis. Data values will be stored as doubles. 
    In the case of discrete variables, the value stored will be 0, 1, ... indicating the variable level. 
    For discrete variables, labels or names corresponding to each variable level would be stored as well. 
    """
    _java_name = java_imports['Trait']
    ## Constructor for trait
    # @param name this trait
    # @param isDiscrete true if this trait is discrete, false if it is continuous
    # @param type the trait type; data, covariate, factor, marker, or exclude
    # @param properties a property map, which can be null
    @javaConstructorOverload(java_imports['Trait'],
                (make_sig([java_imports['String'],'boolean',java_imports['String'],
                           java_imports['Map']],'void'),
                           (metaString,metaBoolean,metaString,Map)),
                (make_sig([java_imports['String'],'boolean',java_imports['String']],'void'),
                 (metaString,metaBoolean,metaString)))
    def __init__(self, *args, **kwargs):
        """
        Constructor for Trait

        Signatures:

        Trait(String name, boolean isDiscrete, String type, Map<String, Object> properties)
        Trait(String name, boolean isDiscrete, String type)

        Arguments:

        Trait(String name, boolean isDiscrete, String type, Map<String, Object> properties)
            name -- this trait
            isDicrete -- true if this trait is discrete, false if it is continuous
            type -- the trait type; data, covariate, factor, marker, or exclude
            properties -- a property map, which can be null
        Trait(String name, boolean isDiscrete, String type)
            name -- this trait
            isDicrete -- true if this trait is discrete, false if it is continuous
            type -- the trait type; data, covariate, factor, marker, or exclude
        """
        super(Trait, self).__init__(*args, generic=(Trait,), **kwargs)
    ## Gets a copy of an existing trait
    # @param trait the trait to be copied
    # @return A copy of the trait
    @javaStaticOverload(java_imports['Trait'],"getInstance",
                        (make_sig([java_imports['Trait']],java_imports['Trait']),
                         (metaTrait,),lambda x: Trait(obj=x)))
    def getInstance(*args):
        """
        Gets a copy of an existing trait

        Signatures:

        static Trait getInstance(Trait trait)

        Arguments:

        trait -- the trait to be copied

        Returns:

        A copy of the trait
        """
        pass
    ## Gets the name by which the trait is identified
    # @return Name by which the trait is identified
    @javaOverload("getName",
                  (make_sig([],java_imports['String']),(),None))
    def getName(self, *args):
        """
        Gets the name by which the trait is identified

        Signatures:

        String getName()

        Returns:

        Name by which the trait is identified
        """
        pass
    ## Gets whether this trait is discrete
    # @return true if this trait is discrete, false if it is continuous
    @javaOverload("isDiscrete",
                  (make_sig([],'boolean'),(),None))
    def isDiscrete(self, *args):
        """
        Gets whether this trait is discrete

        Signatures:

        boolean isDiscrete()

        Returns:

        true if this trait is discrete, false if it is continuous
        """
        pass
    ## Sets the level labels
    # @param levelLabels for a discrete trait, the names of the levels or values this
    # trait can take
    @javaOverload("setLevelLabels",
                  (make_sig([java_imports['String']+'[]'],'void'),
                   (javaArray.get_array_type(String),),None))
    def setLevelLabels(self, *args):
        """
        Sets the level labels

        Signatures:

        void setLevelLabels(String[] levelLabels)

        Arguments:

        levelLabels -- for a discrete trait, the names of the levels or values this trait
                       can take
        """
        pass
    ## Gets the level labels
    # @return For a discrete trait, the names of the levels or values this trait can take
    @javaOverload("getLevelLabels",
                  (make_sig([],java_imports['String']+'[]'),(),
                   String.wrap_existing_array))
    def getLevelLabels(self, *args):
        """
        Gets the level labels

        Signatures:

        String[] getLevelLabels()

        Returns:

        For a discrete trait, the names of the levels or values this trait can take
        """
        pass
    ## Gets the name of a level
    # @param level The level number (0,1,...)
    # @return The name of this level
    @javaOverload("getLevelLabel",
                  (make_sig(['int'],java_imports['String']),(metaInteger,),None))
    def getLevelLabel(self, *args):
        """
        Gets the name of a level

        Signatures:

        String getLevelLabel(int level)

        Arguments:

        level -- the level number (0,1,...)

        Returns:

        The name of this level
        """
        pass
    ## Gets the number of levels
    # @return The number of levels
    @javaOverload("getNumberOfLevels",
                  (make_sig([],'int'),(),None))
    def getNumberOfLevels(self, *args):
        """
        Gets the number of levels

        Signatures:

        int getNumberOfLevels()

        Returns:

        The number of levels
        """
        pass
    ## Gets the number of entries in the property map
    # @return The number of entries in the property map
    @javaOverload("getNumberOfProperties",
                  (make_sig([],'int'),(),None))
    def getNumberOfProperties(self, *args):
        """
        Gets the number of entries in the property map

        Signatures:

        int getNumberOfProperties()

        Returns:

        The number of entries in the property map
        """
        pass
    @javaGenericOverload("getProperties",
                (make_sig([],java_imports['Set']),(),
                 lambda x: Set(obj=x, generic=(Map.Entry,))))
    def _getProperties(self, *args):
        pass
    ## The entry set for this trait's property map
    # @return The entry Set for this trait's property map
    def getProperties(self, *args):
        """
        The entry set for this trait's property map

        Signatures:

        Set<Entry<String, Object>> getProperties()

        Returns:

        The entry Set for this trait's property map
        """
        props = self._getProperties(*args)
        props.generic_dict['/@1/'].generic_dict = {'/@1/':String, '/@2/':Object}
        return props
    ## Gets the value of this property null if property does not exist
    # @param The name of a property for this trait
    # @return The value of this property, null if the property does not exist
    @javaOverload("getProperty",
                  (make_sig([java_imports['String']],java_imports['Object']),
                   (metaString,),lambda x: Object(obj=send_to_java(x))))
    def getProperty(self, *args):
        """
        Gets the value of this property, null if property does not exist

        Signatures:

        Object getProperty(String propertyName)

        Arguments:

        propertyName -- The name of a property for this trait

        Returns:

        The value of this property null if the property does not exist
        """
        pass
    ## Gets all the property names for this trait
    # @return All the property names for this trait
    @javaGenericOverload("getPropertyNames",
                (make_sig([],java_imports['Set']),(),
                 dict(type=Set,generic=(String,))))
    def getPropertyNames(self, *args):
        """
        Gets all the property names for this trait

        Signatures:

        Set<String> getPropertyNames()

        Returns:

        All the property names for this trait
        """
        pass
    ## Adds a property or sets a new value for an existing property
    # @param propertyName a name
    # @param value The value for this property
    @javaOverload("setProperty",
                  (make_sig([java_imports['String'],java_imports['Object']],'void'),
                   (metaString,Object),None))
    def setProperty(self, *args):
        """
        Adds a property or sets a new value for an existing property

        Signatures:

        void setProperty(String propertyName, Object value)

        Arguments:
        
        propertyName -- a name
        value -- The value for this property
        """
        pass
    ## Adds a new factor and its value or changes the value of an existing factor.
    # A factor might be an environment or a rep number
    # @param name This factor's name
    # @param value The factor's value for this trait
    @javaOverload("addFactor",
            (make_sig([java_imports['String'],java_imports['String']],'void'),
             (metaString,metaString),None))
    def addFactor(self, *args):
        """
        Adds a new factor and its value or changes the value of an existing factor.
        A factor might be an environment or a rep number

        Signatures:

        void addFactor(String name, String value)

        Arguments:

        name -- this factor's name
        value -- the factor's value for this trait
        """
        pass
    ## Gets the number of factors for this trait
    # @return The number of factors for this trait
    @javaOverload("getNumberOfFactors",
                  (make_sig([],'int'),(),None))
    def getNumberOfFactors(self, *args):
        """
        Gets the number of factors for this trait

        Signatures:

        int getNumberOfFactors()

        Returns:

        The number of factors for this trait
        """
        pass
    ## Gets the names for the factors for this trait. Returns null if
    # there are no factors
    # @return Names for the factors for this trait or null if there are no factors
    @javaGenericOverload("getFactorNames",
                  (make_sig([],java_imports['ArrayList']),(),
                   dict(type=ArrayList,generic=(String,))))
    def getFactorNames(self, *args):
        """
        Gets the names for the factors for this trait. Returns null if
        there are no factors

        Signatures:

        ArrayList<String> getFactorNames()

        Returns:

        Names for the factors for this trait. Returns null if there
        are no factors
        """
        pass
    ## Gets a factor value
    # @return The value of this factor, or null if the factor does not exist
    @javaOverload("getFactorValue",
                  (make_sig([java_imports['String']],java_imports['String']),
                   (metaString,),None))
    def getFactorValue(self, *args):
        """
        Gets a factor value

        Signatures:

        String getFactorValue(String factorName)

        Returns:

        The value of this factor or null if the factor does not exist
        """
        pass
    ## Gets the type of this trait
    # @return The type of this trait: data, covariate, factor, marker, or exclude
    @javaOverload("getType",
                  (make_sig([],java_imports['String']),(),None))
    def getType(self, *args):
        """
        Gets the type of this trait

        Signatures:

        String getType()

        Returns:

        The type of this trait: data, covariate, factor, marker, or exclude
        """
        pass
    ## Sets the type of this trait
    # @return The type of this trait: data, covariate, factor, marker, or exclude
    @javaOverload("setType",
                  (make_sig([java_imports['String']],'void'),(metaString,),None))
    def setType(self, *args):
        """
        Sets the type of this trait

        Signatures:

        void setType(String type)

        Arguments:

        type -- The type of this trait: data covariate, factor, marker, or exclude
        """
        pass
    ## Returns whether the trait has level
    # @return true if the trait has levels
    @javaOverload("hasLevels",
                  (make_sig([],'boolean'),(),None))
    def hasLevels(self, *args):
        """
        Returns whether the trait has levels

        Signatures:

        boolean hasLevels()

        Returns:

        true if the trait has levels
        """
        pass
