from TASSELpy.net.maizegenetics.plugindef.AbstractPlugin import AbstractPlugin
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaConstructorOverload, javaOverload
from TASSELpy.java.lang.Object import Object
from TASSELpy.java.lang.Boolean import Boolean, metaBoolean
from TASSELpy.java.lang.Double import metaDouble
from TASSELpy.java.lang.Integer import metaInteger
from TASSELpy.java.lang.Long import metaLong
from TASSELpy.java.lang.String import String, metaString

java_imports = {'FixedEffectLMPlugin':'net/maizegenetics/analysis/association/FixedEffectLMPlugin',
                'Frame':'java/awt/Frame',
                'String':'java/lang/String'}

class FixedEffectLMPlugin(AbstractPlugin):
    _java_name = java_imports['FixedEffectLMPlugin']
    @javaConstructorOverload(java_imports['FixedEffectLMPlugin'],
                             (make_sig([java_imports['Frame'],'boolean'],'void'),
                              (Object,metaBoolean)))    
    def __init__(self, *args, **kwargs):
        """ Creates a new instance of FixedEffectLMPlugin

        Signatures:

        FixedEffectLMPlugin(Frame parentFrame, boolean isInteractive)

        Arguments:

        parentFrame -- A frame, can be null
        isInteractive -- Whether in an interactive session
        """
        pass
    @javaOverload("setOutputFile",
                  (make_sig([java_imports['String']],'void'),(metaString,),None))
    def setOutputFile(self, *args):
        """ Sets the output file

        Signatures:

        void setOutputFile(String filename)

        Arguments:

        filename -- the name of the filename
        """
        pass
    @javaOverload("setRestrictOutput",
                  (make_sig(['boolean'],'void'),(metaBoolean,),None))
    def setRestrictOutput(self, *args):
        """ Set the output to be restricted (or not)

        Signatures:

        void setRestrictOutput(boolean restrict)

        Arguments:

        restrict -- whether to restrict the output
        """
        pass
    @javaOverload("setMaxP",
                  (make_sig(['double'],'void'),(metaDouble,),None))
    def setMaxP(self, *args):
        """ Sets the maximum value of the p-value to keep

        Signatures:

        void setMaxP(double value)

        Arguments:

        value -- the maximum p-value
        """
        pass
    @javaOverload("setPermute",
                  (make_sig(['boolean'],'void'),(metaBoolean,),None))
    def setPermute(self, *args):
        """ Sets whether to perform permutations

        Signatures:

        void setPermute(boolean permute)

        Arguments:

        permute -- Whether to perform permutations
        """
        pass
    @javaOverload("setNumberOfPermutations",
                  (make_sig(['int'],'void'),(metaInteger,),None))
    def setNumberOfPermutations(self, *args):
        """ Sets the number of permutations to perform

        Signatures:

        void setNumberOfPermutations(int numberOfPermutations)

        Arguments:

        numberOfPermutations -- the number of permutations to perform
        """
        pass
    @javaOverload("setRandomizer",
                  (make_sig(['long'],'void'),(metaLong,),None))
    def setRandomizer(self, *args):
        """ Sets the randomizer seed so that permutation results are reproducible
        for testing. The same seed will reproduce the same sequence of pseudo-random
        numbers

        Signatures:

        void setRandomizer(long seed)

        Arguments:

        seed -- the seed
        """
        pass
