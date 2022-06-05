from asymmetryFactorJ1.structures import *


class J1Gauss(J1Attributes):
    def __init__(self, x, m, ur, k, z0, s) -> None:
        super().__init__(x, m, ur)

        self.k = k
        self.z0 = z0
        self.s = s
        pass

    def print_j1_gauss_attributes(self):
        print("x: ", self.x)
        print("M: ", self.M)
        print("Ur: ", self.ur)
        print("k: ", self.k)
        print("z0: ", self.z0)
        print("s: ", self.s)
