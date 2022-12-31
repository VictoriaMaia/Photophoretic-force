class ParticleAttributes:
    def __init__(self, x, m, ur) -> None:
        self.x = x
        self.M = m
        self.ur = ur
        pass

    def print_particle_attributes(self):
        print("x: ", self.x)
        print("M: ", self.M)
        print("Ur: ", self.ur)
