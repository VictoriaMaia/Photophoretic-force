from AsymmetryFactor.beams.beam_class import BeamAttributes

class FrozenWaveAttributes(BeamAttributes):
    def __init__(self, k, z0, q, l, n, name="Frozen Wave Beam") -> None:
        super().__init__(name)

        self.k = k
        self.z0 = z0
        self.q = q
        self.l = l 
        self.n = n
        pass

    def print_beam_attributes(self):
        print("k: ", self.k)
        print("z0: ", self.z0)
        print("q: ", self.q)
        print("l: ", self.l)
        print("n: ", self.n)
        print()

    def beam_info(self):
        return f'name:{self.name}'
