import abc


class BeamAttributes:
    def __init__(self, name, k=None, z0=None, metaclass=abc.ABCMeta) -> None:
        self.name = name
        self.k = k
        self.z0 = z0
        pass


    def print_beam_name(self):
        print("Name: ", self.name)


    @abc.abstractmethod
    def gn(self, n):
        ...