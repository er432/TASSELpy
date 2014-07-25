from TASSELpy.net.maizegenetics.util.OpenBitSet import OpenBitSet
from TASSELpy.javaObj import javaObj
from TASSELpy.utils.helper import make_sig
from TASSELpy.utils.Overloading import javaOverload
from TASSELpy.java.lang.String import String
from TASSELpy.java.lang.Long import Long
import javabridge
import numpy as np



## Dictionary to hold java imports
java_imports = {'genotypecall':'net/maizegenetics/dna/snp/genotypecall', 
		'GenotypeCallTable':'net/maizegenetics/dna/snp/genotypecall/GenotypeCallTable'
		'String':'java/lang/String',
		'Object':'java/lang/Object',
		'Boolean':'java/lang/Boolean'}

class GenotypeCallTable(javaObj):
	@javaOverload("genotype", (make_sig(['int', 'int'], 'byte'), (int, int), None))
	def genotype(self, *args):
		pass

	@javaOverload("genotypeArray", (make_sig(['int', 'int'], 'byte[]'), (int, int), None))
	def genotypeArray(self, *args):
		pass

	@javaOverload("genotypeRange",(make_sig(['int','int','int'],'byte[]'),(int, int, int),None))
    	def genotypeRange(self, *args):
		pass

	@javaOverload("genotypeAllSites",(make_sig(['int'],'byte[]'),(int,),None))
    	def genotypeAllSites(self, *args):
		pass

	@javaOverload("genotypeAsString",(make_sig(['int','int'],java_imports['String']),(int,int),None),
                  (make_sig(['int','byte'],java_imports['String']),(int,np.int8),None))
    	def genotypeAsString(self, *args):	
		pass
	
	@javaOverload("genotypeAsStringRange",(make_sig(['int','int','int'],java_imports['String']),	
			(int,int,int),None))
    	def genotypeAsStringRange(self, *args):
		pass

	@javaOverload("genotypeAsStringRow",(make_sig(['int'],java_imports['String']),(int,),None))
    	def genotypeAsStringRow(self, *args):
		pass

	@javaOverload("genotypeAsStringArray",(make_sig(['int','int'],java_imports['String']+'[]'),
			(int,int),lambda x: map(lambda y: javabridge.get_env().get_string(y),
                                 javabridge.get_env().get_object_array_elements(x))))
    	def genotypeAsStringArray(self, *args):
		pass


	@javaOverload("isHeterozygous", (make_sig(['int', 'int'], 'boolean'),(int, int), 	
			None))
	def isHeterozygous(self, *args):
		pass


	@javaOverload("isPolymorphic", (make_sig(['int'], 'boolean'),(int,),None))
	def isPolymorphic(self, *args):
		pass

	@javaOverload("isPhased", (make_sig([],'boolean'),(None),None))
	def isPhased(self, *args):
		pass

	@javaOverload("retainsRareAlleles", (make_sig([],'boolean'),(None),None))
	def retainsRareAlleles(self, *args):
		pass

	@javaOverload("alleleDefinitions",(make_sig([],java_imports['String']+'[][]'),(), 
        	lambda x: map(lambda z: map(lambda y: String(obj=y).toString(),
            	javabridge.get_env().get_object_array_elements(z)),
            	javabridge.get_env().get_object_array_elements(x))),
            	(make_sig(['int'],java_imports['String']+'[]'),(int,),
        	lambda x: np.array(map(lambda y: String(obj=y).toString(),
                javabridge.get_env().get_object_array_elements(x)))))
    	def alleleDefinitions(self, *args):
		pass

	
	@javaOverload("diploidAsString",(make_sig(['int','byte'],java_imports['String']),(int,np.int8),
                   None))
    	def diploidAsString(self, *args):
		pass

	@javaOverload("maxNumAlleles",(make_sig([],'int'),(),None))
    	def maxNumAlleles(self, *args):
		pass

	@javaOverload("totalGametesNonMissingForSite",(make_sig(['int'],'int'),(int,),None))
    	def totalGametesNonMissingForSite(self, *args):
		pass

	@javaOverload("totalNonMissingForSite",(make_sig(['int'],'int'),(int,),None))
    	def totalNonMissingForSite(self, *args):
		pass

	@javaOverload("minorAllele",(make_sig(['int'],'byte'),(int,),None))
    	def minorAllele(self, *args):
		pass

	@javaOverload("minorAlleleCount",(make_sig(['int'],'int'),(int,),None))
    	def minorAlleleCount(self, *args):
		pass

	@javaOverload("majorAlleleCount",(make_sig(['int'],'int'),(int,),None))
    	def majorAlleleCount(self, *args):
		pass

	 @javaOverload("genoCounts",(make_sig([],java_imports['Object']+'[][]'),(),
                lambda x: [np.array(map(lambda y: String(obj=y).toString(),
                javabridge.get_env().get_object_array_elements(\
                javabridge.get_env().get_object_array_elements(x)[0]))),
                np.array(map(lambda y: Long(obj=y).longValue(),
                javabridge.get_env().get_object_array_elements(\
                javabridge.get_env().get_object_array_elements(x)[1])))]))
    	def genoCounts(self, *args):
		pass

	@javaOverload("majorMinorCounts",(make_sig([],java_imports['Object']+'[][]'),(),
                lambda x: [np.array(map(lambda y: String(obj=y).toString(),
                javabridge.get_env().get_object_array_elements(\
                javabridge.get_env().get_object_array_elements(x)[0]))),
                np.array(map(lambda y: Long(obj=y).longValue(),
                javabridge.get_env().get_object_array_elements(\
                javabridge.get_env().get_object_array_elements(x)[1])))]))
    	def majorMinorCounts(self, *args):
		pass

	@javaOverload("totalGametesNonMissingForTaxon",(make_sig(['int'],'int'),(int,),None))
    	def totalGametesNonMissingForTaxon(self, *args):
		pass

	@javaOverload("heterozygousCountForTaxon",(make_sig(['int'],'int'),(int,),None))
    	def heterozygousCountForTaxon(self, *args):
		pass

	@javaOverload("totalNonMissingForTaxon",(make_sig(['int'],'int'),(int,),None))
    	def totalNonMissingForTaxon(self, *args):
		pass

	@javaOverload("allelesSortedByFrequency",(make_sig(['int'],'int[][]'),(int,),
                   lambda x: map(lambda y: javabridge.get_env().get_int_array_elements(y),
                   javabridge.get_env().get_object_array_elements(x))))
    	def allelesSortedByFrequency(self, *args):
		pass

	@javaOverload("genosSortedByFrequency",(make_sig(['int'],java_imports['Object']+'[][]'),(int,),
                   lambda x: [np.array(map(lambda y: javabridge.call(y,"toString","()Ljava/lang/String;"),
                   javabridge.get_env().get_object_array_elements(\
                   javabridge.get_env().get_object_array_elements(x)[0]))),
                   np.array(map(lambda y: javabridge.call(y,"intValue","()I"),
                   javabridge.get_env().get_object_array_elements(\
                   javabridge.get_env().get_object_array_elements(x)[1])))]))
    	def genosSortedByFrequency(self, *args):
		pass

	@javaOverload("alleles",(make_sig(['int'],'byte[]'),(int,),None))
    	def alleles(self, *args):	
		pass

	@javaOverload("majorAlleleForAllSites", (make_sig([], 'byte'), (None), None))
	def majorAlleleForAllSites(self, *args):
		pass
	
	@javaOverload("minorAlleleForAllSites", (make_sig([], 'byte'), (None), None))
	def minorAlleleForAllSites(self, *args):
		pass
	
	@javaOverload("majorAllele",(make_sig(['int'],'byte'),(int,),None))
    	def majorAllele(self, *args):
		pass	

	@javaOverload("minorAlleleAsString",(make_sig(['int'],java_imports['String']),(int,),None))
    	def minorAlleleAsString(self, *args):
		pass

	@javaOverload("majorAlleleAsString",(make_sig(['int'],java_imports['String']),(int,),None))
    	def majorAlleleAsString(self, *args):
		pass
	
	@javaOverload("minorAlleles",(make_sig(['int'],'byte[]'),(int,),None))
    	def minorAlleles(self, *args):
		pass

	@javaOverload("minorAlleleFrequency",(make_sig(['int'],'double'),(int,),None))
    	def minorAlleleFrequency(self, *args):
		pass

	@javaOverload("majorAlleleFrequency",(make_sig(['int'],'double'),(int,),None))
    	def majorAlleleFrequency(self, *args):
		pass

	@javaOverload("numberOfSites",(make_sig([],'int'),(),None))
    	def numberOfSites(self, *args):
		pass

	@javaOverload("numberOfTaxa",(make_sig([],'int'),(),None))
    	def numberOfTaxa(self, *args):
		pass

	@javaOverload("genotypeForAllSites",(make_sig(['int'],'byte[]'),(int),None))
    	def genotypeForAllSites(self, *args):
		pass

	@javaOverload("genotypeForSiteRange",(make_sig(['int', 'int', 'int'],'byte[]'),(int, int, 
		int),None))
    	def genotypeForSiteRange(self, *args):
		pass

	@javaOverload("genotypeForAllTaxa",(make_sig(['int'],'byte[]'),(int),None))
    	def genotypeForAllTaxa(self, *args):
		pass

	@javaOverload("transposeData", (make_sig(['boolean'],()), (boolean), None))
	def transposeData(self, *args):
		pass











