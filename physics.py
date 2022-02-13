import math


class Measurement:

    def measure_distance(self, x, y):
        return  math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)


class Physics(Measurement):

    def update_circle_object(self):
        self.all_object[self.name] = (self.mass, self.x, self.y, self.radius)

    def gravity(self, mass, x, y, r):
        self.speedx += mass * (x - self.x) / r ** 3  # Fx
        self.speedy += mass * (y - self.y) / r ** 3  # Fy
        self.x += self.speedx
        self.y += self.speedy

    def collision(self, obj, r):
        if r < (self.radius + obj.radius):
            self.speedx += obj.speedx
            self.speedy += obj.speedy
            return True
        else:
            return False

    def absorption(self, obj):
        if self.mass == max(self.mass, obj.mass):
            S_self = math.pi * self.radius ** 2
            S_obj = math.pi * obj.radius ** 2
            S_0 = S_self + S_obj
            self.mass += obj.mass
            self.radius = int(math.sqrt(S_0 / math.pi))
            planets.remove(obj)


class Planet(Physics):

    def __init__(self, name, mass, radius, pos: tuple, speed: tuple, color):
        self.color = color
        self.name = name
        self.mass = mass
        self.radius = radius
        self.x = pos[0]
        self.y = pos[1]
        self.speedx = speed[0]
        self.speedy = speed[1]

    def update(self):
        for obj in planets:
            if obj.name != self.name:
                r = self.measure_distance(obj.x, obj.y)
                if self.collision(obj, r):
                    print("collition")
                    self.absorption(obj)
                self.gravity(obj.mass, obj.x, obj.y, r)



planets = [
# Star system
Planet("Sun", 5000, 50, (600, 400), (0, 0), (255, 100, 100)),
Planet("mercury", 50, 5, (600, 200), (-2.5, 0), (255, 10, 100)),
Planet("Venus", 60, 6, (600, 900), (1.5, 0), (236, 193, 19)),
Planet("Earth", 100, 10, (1400, 400), (0, -1.3), "blue"),
Planet("Mars", 80, 8, (-600, 400), (0, 1), "red")
# collade test
#     Planet("P1", 50, 5, (635, 368), (0, 0), "green"),
#     Planet("P1", 50, 5, (435, 365), (0, 0), "blue"),
#     Planet("S1", 100, 10, (412, 556), (0, 0), (255, 100, 100)),
#     Planet("S2", 100, 10, (648, 548), (0, 0), 'red')
          ]

