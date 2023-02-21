class ParticleAttributes:
    def __init__(self, x, m, ur) -> None:
        self.x = x
        self.m = m
        self.ur = ur
        pass

    def print_particle_attributes(self):
        print("x: ", self.x)
        print("m: ", self.m)
        print("Ur: ", self.ur)
        print()

    def particle_info(self):
        return f'x:{self.x}|m:{self.m}'
