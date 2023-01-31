from AsymmetryFactor.beams.beam_class import BeamAttributes

class BesselAttributes(BeamAttributes):
    def __init__(self, k, z0, angle, name="Bessel Beam") -> None:
        super().__init__(name)

        self.k = k
        self.z0 = z0
        self.angle = angle
        pass

    def print_bessel_attributes(self):
        print("k: ", self.k)
        print("z0: ", self.z0)
        print("angle: ", self.angle)
