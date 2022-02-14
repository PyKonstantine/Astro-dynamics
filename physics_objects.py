from physics import Physics


class Planet(Physics):

    def __init__(self, name, mass, radius, pos: tuple, speed: tuple, color):
        super().__init__()
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
                    self.absorption(obj)
                self.gravity(obj.mass, obj.x, obj.y, r)

    def remove(self):
        planets.remove(self)


#  --------------------------------------------objects-init-------------------------------------------------------------

planets = [
    # Star system
    # Planet("Sun", 5000, 50, (600, 400), (0, 0), (255, 100, 100)),
    # Planet("mercury", 50, 5, (600, 200), (-2.5, 0), (255, 10, 100)),
    # Planet("Venus", 60, 6, (600, 900), (1.5, 0), (236, 193, 19)),
    # Planet("Earth", 100, 10, (1400, 400), (0, -1.3), "blue"),
    # Planet("Mars", 80, 8, (-600, 400), (0, 1), "red")

    # collate test
    Planet("P1", 50, 5, (635, 368), (0, 0), "green"),
    # Planet("P1", 50, 5, (435, 365), (0, 0), "blue"),
    # Planet("S1", 100, 10, (412, 556), (0, 0), (255, 100, 100)),
    Planet("S2", 100, 10, (648, 548), (0, 0), 'red'),
    Planet("S3", 100, 10, (550, 251), (0, 0), 'yellow'),
    Planet("S4", 300, 15, (650, 251), (0, 0), 'white'),
    # Planet("P1", 50, 5, (535, 368), (0, 0), "blue"),
    # Planet("P1", 50, 5, (635, 468), (0, 0), "green")
          ]
