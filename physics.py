import math


class Measurement:

    def __init__(self):
        self.x = None
        self.y = None

    def measure_distance(self, x, y):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)


class Physics(Measurement):

    def __init__(self):
        super().__init__()
        self.radius = None
        self.mass = None
        self.speedx = None
        self.speedy = None

    def gravity(self, mass, x, y, r):
        self.speedx += mass * (x - self.x) / r ** 3  # Fx
        self.speedy += mass * (y - self.y) / r ** 3  # Fy
        self.x += self.speedx
        self.y += self.speedy

    def collision(self, obj, r):
        if r < (self.radius + obj.radius):
            x1 = ((self.mass - obj.mass) * self.speedx) / (self.mass + obj.mass)
            y1 = ((self.mass - obj.mass) * self.speedy) / (self.mass + obj.mass)
            x2 = (2 * self.mass * self.speedx) / (self.mass + obj.mass)
            y2 = (2 * self.mass * self.speedy) / (self.mass + obj.mass)
            self.speedx = x1 * 1.3
            self.speedy = y1 * 1.3
            obj.speedx = x2 * 1.3
            obj.speedy = y2 * 1.3
            return True

    def absorption(self, obj):
        if self.mass == max(self.mass, obj.mass):
            s_self = math.pi * self.radius ** 2
            s_obj = math.pi * obj.radius ** 2
            s_0 = s_self + s_obj
            self.mass += obj.mass
            self.radius = int(math.sqrt(s_0 / math.pi))
            obj.remove()
