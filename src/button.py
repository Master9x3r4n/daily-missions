
import pygame as pg
import math

pg.init()
pg.font.init()

class Button:
    def __init__(self, x, y, surface, radius = 32, text = "", font_size = 64, color = "#FFFFFF",text_color = "#000000"):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        font = pg.font.SysFont("Arial", font_size)
        self.text_surface = font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=(x, y))
        self.surface = surface

    def draw(self):
        pg.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)
        self.surface.blit(self.text_surface, self.text_rect)

    def is_clicked(self, event):
        if event.type != pg.MOUSEBUTTONDOWN or event.button != 1:
            return False

        mx, my = event.pos
        return math.hypot(mx - self.x, my - self.y) <= self.radius