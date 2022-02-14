import random
import pygame as pg


class Graphic:

    pg.display.set_caption("Astro dynamics")
    WIDTH = 1200  # 1920
    HEIGHT = 800  # 1080
    FPS = 60

    def __init__(self):
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT), pg.RESIZABLE)
        self.background = b.get_stars()
        self.font = pg.font.Font(None, 15)
        self.cam_x = 0
        self.cam_y = 0
        self.zoom = 1
        self.back_x = 0
        self.back_y = 0

    def cam_move(self, key):
        if key[pg.K_UP]:
            self.cam_y -= 2 / self.zoom * 2
            self.back_y -= 0.1
        if key[pg.K_DOWN]:
            self.cam_y += 2 / self.zoom * 2
            self.back_y += 0.1
        if key[pg.K_LEFT]:
            self.cam_x -= 2 / self.zoom * 2
            self.back_x -= 0.1
        if key[pg.K_RIGHT]:
            self.cam_x += 2 / self.zoom * 2
            self.back_x += 0.1

    def cam_zoom(self, key):
        if key[pg.K_HOME]:
            self.zoom = self.zoom * 1.01
        if key[pg.K_END]:
            self.zoom = self.zoom * 0.99
        if self.zoom < 0:
            self.zoom = 0

    def blit_text(self, text: str, pos: tuple, color=(255, 255, 255)):
        text_img = self.font.render(text, True, color)
        self.screen.blit(text_img, pos)

    def background_draw(self):
        for s in self.background:
            pg.draw.circle(self.screen, s.color, (s.x - self.back_x * s.distance, s.y - self.back_y * s.distance), s.radius)

    def display(self, circle):
        self.screen.fill((0, 0, 0))

        self.background_draw()
    # ------------------------------------zoom-display--------------------------------------

        for obj in circle:
            normal_x = self.zoom * (-(self.WIDTH / 2) + (obj.x - self.cam_x))
            normal_y = self.zoom * ((self.HEIGHT / 2) - (obj.y - self.cam_y))
            zoomx = 1200 / 2 + normal_x
            zoomy = 800 / 2 - normal_y

            if zoomx > self.WIDTH or zoomx < 0 or zoomy > self.HEIGHT or 0 > zoomy:
                pass
            else:
                pg.draw.circle(self.screen, obj.color, (zoomx, zoomy), obj.radius * self.zoom)

    # ---------------------------------------------------------------------------------------

        self.blit_text(f'fps: {int(self.clock.get_fps())}', (10, 10))
        self.blit_text(f'zoom: {round(self.zoom, 3)}', (10, 30))

        pg.display.update()
        self.clock.tick(self.FPS)


class Background:

    """ надо реализовать появления и исчезновение звезд вышедших за границу экрана"""
    stars = []

    def __init__(self):
        self.x = None
        self.y = None
        self.color = None
        self.distance = None
        self.radius = 1

    def random_position_init(self):
        self.x = random.randint(0, Graphic.WIDTH)
        self.y = random.randint(0, Graphic.HEIGHT)
        self.color = random.choice([
            'yellow', 'white', 'orange'
        ])
        self.distance = random.choice([0.1, 1, 0.5])
        # self.radius = random.randint(1, 2)

    def init(self, number):
        for i in range(number):
            s = Background()
            s.random_position_init()
            self.stars.append(s)

    def get_stars(self):
        return self.stars


b = Background()
b.init(300)
