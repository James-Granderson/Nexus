# nexus.py
# The spatial architecture of the Nexus simulation.

class Court:
    def __init__(self):
        self.length = 94.0
        self.width = 50.0
        self.sideline_x = 25.0
        self.baseline_y = 47.0
        self.floor_z = 0.0

class Arena:
    def __init__(self, name: str, total_width: float, total_length: float, ceiling_z: float):
        self.name = name
        self.total_width = total_width
        self.total_length = total_length
        self.center_x = 0.0
        self.center_y = 0.0
        self.ceiling_z = ceiling_z

        # The court is a fixed object inside every arena
        self.court = Court()

class Player:
    def __init__(self, name: str, x: float, y: float, court: Court, z: float):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

# Why this exists:
# Arena is a parameterized container (footprint + optional ceiling).
# Court defines the playing surface (x/y bounds + floor_z).
# Player exists in 3D space; z defaults to the court floor.
# The simulation accepts an Arena instance.
# It doesn't care if it's MSG, Crypto, or a random high school gym.
# It just reads the dimensions and acts accordingly.
