import sys
import pygame as pg
from graphic import Graphic
from physics_objects import planets


class App:

    pg.init()

    def __init__(self):
        self.graphic = Graphic()
        self.planets = planets
        self.running = True

    @staticmethod
    def exit(key):
        if key[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()

    def run(self):

        while self.running:

            key = pg.key.get_pressed()

            self.graphic.cam_move(key)
            self.graphic.cam_zoom(key)
            self.graphic.background.cam_move(key)
            self.exit(key)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    print(f'{pg.mouse.get_pos()}')

            for obj in self.planets:
                obj.update()

            self.graphic.display(self.planets)


if __name__ == "__main__":
    app = App()
    app.run()
