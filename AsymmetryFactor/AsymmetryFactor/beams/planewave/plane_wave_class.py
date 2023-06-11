from AsymmetryFactor.beams.beam_class import BeamAttributes

class PlaneWaveAttributes(BeamAttributes):
    def __init__(self, name="Plane Wave") -> None:
        super().__init__(name)
        pass

    def gn(self, n):
        return 1
