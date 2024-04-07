class Punkt:
    def __init__(self, px , py):
        self.x = px
        self.y = py

    def __eq__n__(self, other):
        return self.x == other.x and self.y == other.y
