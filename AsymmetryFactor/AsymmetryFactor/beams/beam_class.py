class BeamAttributes:
    def __init__(self, name="Plane Wave") -> None:
        self.name = name
        pass

    def print_beam_attributes(self):
        print("Name: ", self.name)

    def beam_info(self):
        return f'name:{self.name}'
    
    def gn_beam(self):
        ...