#TASSELpy
##Author: Eli Rodgers-Melnick

TASSELpy is a Python API for the Java program TASSEL 5. 

Documentation: http://pythonhosted.org/tasselpy

Download: https://pypi.python.org/pypi/tasselpy

Dependencies: 

numpy

javabridge (http://pythonhosted.org/javabridge)

Installation:

pip install -U tasselpy

Example:
```python
import os
from TASSELpy.TASSELbridge import TASSELbridge
TASSELbridge.start()
from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
from TASSELpy.net.maizegenetics.dna.WHICH_ALLELE import WHICH_ALLELE

home_dir=os.path.expanduser('~')
tassel_dir=os.path.join(home_dir,'bioinformatics','tassel5-standalone')
geno_file=os.path.join(tassel_dir,'TASSELTutorialData','data','mdp_genotype.hmp.txt')
genoTable = ImportUtils.readGuessFormat(geno_file)
genoTable.genotype(0,0)
majorBits = genoTable.allelePresenceForAllSites(0,
                WHICH_ALLELE.Major)
majorBits.getBits()
TASSELbridge.stop()
```



