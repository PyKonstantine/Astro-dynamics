import os.path
import random
import pygame as pg

folder_path = os.path.dirname(__file__)
picture_folder = os.path.join(folder_path, 'image')
milkyway = pg.image.load(os.path.join(picture_folder, 'milkyway.jpg'))


class BackgroundStars:

    stars = []
    cam_x = 0
    cam_y = 0

    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = (0, 0, 0)
        self.distance = 1
        self.radius = 1

    def random_position_init(self, w, h):
        self.x = random.randint(0, w)
        self.y = random.randint(0, h)
        self.color = random.choice([(255, 255, 200), (255, 255, 255), (255, 200, 200), (255, 200, 0), (200, 200, 255)])
        self.distance = random.choice([2.5, 1.1, 1.7, 1.05, 1.35, 1.005, 1.5, 1.45])
        self.radius = random.randint(1, 2)

    def set_stars_number(self, number, width, height):
        for i in range(number):
            s = BackgroundStars()
            s.random_position_init(width, height)
            self.stars.append(s)

    def draw(self, screen, w, h):
        for s in self.stars:
            x = s.x + self.cam_x / s.distance
            y = s.y + self.cam_y / s.distance
            if x > w:
                s.x -= w
            if x < 0:
                s.x += w
            if y > h:
                s.y -= h
            if y < 0:
                s.y += h
            pg.draw.rect(screen, s.color, (x, y, s.radius, s.radius))

    def cam_move(self, key):
        if key[pg.K_UP]:
            self.cam_y += 0.3
        if key[pg.K_DOWN]:
            self.cam_y -= 0.3
        if key[pg.K_LEFT]:
            self.cam_x += 0.3
        if key[pg.K_RIGHT]:
            self.cam_x -= 0.3


class Graphic:

    pg.display.set_caption("Astro dynamics")
    FULL_SCREEN = -2147483648
    RESIZABLE = 16

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = 60
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT), self.RESIZABLE)
        self.milkyway_img = pg.transform.scale(milkyway, (self.WIDTH, self.HEIGHT)).convert_alpha()
        self.milkyway_img.set_alpha(100)
        self.background = BackgroundStars()
        self.background.set_stars_number(500, self.WIDTH, self.HEIGHT)
        self.font = pg.font.Font(None, 15)
        self.cam_x = 0
        self.cam_y = 0
        self.zoom = 0.3

    def cam_move(self, key):
        if key[pg.K_UP]:
            self.cam_y -= 2 / self.zoom * 2
        if key[pg.K_DOWN]:
            self.cam_y += 2 / self.zoom * 2
        if key[pg.K_LEFT]:
            self.cam_x -= 2 / self.zoom * 2
        if key[pg.K_RIGHT]:
            self.cam_x += 2 / self.zoom * 2

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

    def draw_interface(self):
        self.blit_text(f'fps: {int(self.clock.get_fps())}', (10, 10))
        self.blit_text(f'zoom: {round(self.zoom, 3)}', (10, 30))
        self.blit_text('to move cam press (up) (down) (left) (right) button', (self.WIDTH - 250, 10))
        self.blit_text('to zoom press (home) (end) button', (self.WIDTH - 176, 30))

    def draw_circle(self, obj):

        for o in obj:
            normal_x = self.zoom * (-(self.WIDTH / 2) + (o.x - self.cam_x))
            normal_y = self.zoom * ((self.HEIGHT / 2) - (o.y - self.cam_y))
            zoomx = 1200 / 2 + normal_x
            zoomy = 800 / 2 - normal_y

            if zoomx > self.WIDTH or zoomx < 0 or zoomy > self.HEIGHT or 0 > zoomy:
                pass
            else:
                pg.draw.circle(self.screen, o.color, (zoomx, zoomy), o.radius * self.zoom)

    def display(self, circle):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.milkyway_img, (0, 0))
        self.background.draw(self.screen, self.WIDTH, self.HEIGHT)

        self.draw_circle(circle)

        pg.display.update()
        self.clock.tick(self.FPS)
