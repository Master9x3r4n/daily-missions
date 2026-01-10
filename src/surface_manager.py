import pygame as pg

pg.init()
pg.font.init()

class SurfaceManager:
    def __init__(self):
        self.WIDTH = 1152
        self.HEIGHT = 648
        self.SURFACE = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("Daily Missions")

    def draw_rect (self, color, rect):
        #draw rect
        pg.draw.rect(self.SURFACE, color, rect)

    def draw_circle (self, color, x: float, y: float, radius: float):
        #draw circle
        pg.draw.circle(self.SURFACE, color, (x, y), radius)

    def draw_text (self, font, string, x, y, color = "#000000"):
        #draw text
        text_surface = font.render(string, True, color)
        self.SURFACE.blit(text_surface, (x, y))

    def draw_menu(self):
        self.draw_rect("#FFFFFF", (0, 0, self.WIDTH, self.HEIGHT * 0.5))