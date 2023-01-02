from AsymmetryFactor.beams.beam_class import BeamAttributes

class GaussAttributes(BeamAttributes):
    def __init__(self, k, z0, s, name="Gaussian Beam") -> None:
        super().__init__(name)

        self.k = k
        self.z0 = z0
        self.s = s
        pass

    def print_gauss_attributes(self):
        print("k: ", self.k)
        print("z0: ", self.z0)
        print("s: ", self.s)
