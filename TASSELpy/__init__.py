from TASSELpy.TASSELbridge import TASSELbridge
try:
    from TASSELpy.net.maizegenetics.analysis.association.FixedEffectLMPlugin import easy_GLM
except AssertionError:
    TASSELbridge.start()
except AttributeError:
    TASSELbridge.start()
