import pygame as pg


class Graphic:

    pg.display.set_caption("Astro dynamics")

    def __init__(self):
        self.WIDTH = 1200  # 1920
        self.HEIGHT = 800  # 1080
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT), pg.RESIZABLE)
        self.font = pg.font.Font(None, 15)
        self.cam_x = 0
        self.cam_y = 0
        self.zoom = 1

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

    def display(self, circle):
        self.screen.fill((0, 0, 0))

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
