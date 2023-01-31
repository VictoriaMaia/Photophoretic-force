class BeamAttributes:
    def __init__(self, name="Plane Wave") -> None:
        self.name = name
        pass

    def print_beam_name(self):
        print("Name: ", self.name)
