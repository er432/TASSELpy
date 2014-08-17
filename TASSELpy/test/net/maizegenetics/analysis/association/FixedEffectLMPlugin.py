import unittest
import javabridge
from TASSELpy.TASSELbridge import TASSELbridge
try:
    try:
        javabridge.get_env()
    except AttributeError:
        TASSELbridge.start()
    except AssertionError:
        TASSELbridge.start()
except:
    raise RuntimeError("Could not start JVM")
from TASSELpy.net.maizegenetics.analysis.association.FixedEffectLMPlugin import easy_GLM
from TASSELpy.data.data_constants import *
from TASSELpy.net.maizegenetics.dna.snp.ImportUtils import ImportUtils
from TASSELpy.net.maizegenetics.trait.ReadPhenotypeUtils import ReadPhenotypeUtils
debug = False

class easy_GLMTest(unittest.TestCase):
    def test_easy_GLM(self):
        if debug: print("Testing easy_GLM")
        inputAlign = ImportUtils.readFromHapmap(HAPMAP_FILE)
        traits = ReadPhenotypeUtils.readGenericFile(TRAITS_FILE)
        pop = ReadPhenotypeUtils.readGenericFile(POP_STRUCTURE_FILE)
        glm = easy_GLM()
        glm.addPhenotype(traits,'traits')
        glm.addMarkers(inputAlign, 'markers')
        glm.addCovariate(pop,'populations')
        marker_effects, allele_effects = glm.run_glm(phenotypes=('traits',),
                                                     markers='markers',
                                                     covariates=('populations',))
        self.assertAlmostEqual(marker_effects[0,'marker_p'], 0.43840160640231907)
        self.assertAlmostEqual(marker_effects[2,'marker_p'], 0.7049479924759525)

if __name__ == "__main__":
    debug = True
    unittest.main(exit=False)
    TASSELbridge.stop()
