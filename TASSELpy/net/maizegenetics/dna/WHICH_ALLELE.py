from TASSELpy.java.lang.Enum import enum as java_enum

java_imports = {'WHICH_ALLELE':'net/maizegenetics/dna/WHICH_ALLELE'}
## WHICH_ALLELE enum
WHICH_ALLELE=java_enum(java_imports['WHICH_ALLELE'],
                       "Major","Minor","GlobalMajor","GlobalMinor",
                       "Reference","Alternate","HighCoverage","LowCoverage",
                       "Minor2","Minor3","Minor4","Minor5","Ancestral",
                       subclass='WHICH_ALLELE')
