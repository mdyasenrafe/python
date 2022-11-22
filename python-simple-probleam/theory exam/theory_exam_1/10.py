class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        return ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5


print(Distance(2, 10, 5, 6).distance())
