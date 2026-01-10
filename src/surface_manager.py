import pygame as pg
from button import Button

pg.init()
pg.font.init()

class SurfaceManager:
    def __init__(self):
        self.WIDTH = 1152
        self.HEIGHT = 648
        self.WR = self.WIDTH / 1920
        self.HR = self.HEIGHT / 1080
        self.SURFACE = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("Daily Missions")

        self.button_back: Button = None
        self.button_add: Button = None
        self.button_reset: Button = None
        self.button_next: Button = None
        self.init_buttons()

    ##################
    #     SHAPES     #
    ##################
    def draw_rect (self, color, rect, border_radius = 0):
        #draw rect
        pg.draw.rect(self.SURFACE, color, rect, border_radius=border_radius)

    def draw_circle (self, color, x: float, y: float, radius: float):
        #draw circle
        return pg.draw.circle(self.SURFACE, color, (x, y), radius)

    def draw_text (self, font, string, x, y, color = "#000000"):
        #draw text
        text_surface = font.render(string, True, color)
        self.SURFACE.blit(text_surface, (x, y))

    def create_button (self, button_color, x, y, text = "", font_color = "#000000", font_size = 64):
        return Button(x, y, text = text, font_size = font_size, color= button_color, text_color= font_color, surface=self.SURFACE)

    ##################
    #     PANELS     #
    ##################
    def draw_background(self):
        # bg color
        self.draw_rect("#D9D9D9", (0, 0, self.WIDTH, self.HEIGHT))

    def draw_progress_bar(self):
        #progress bar
        self.draw_rect("#FFFFFF", (136 * self.WR, 58 * self.HR, 1760 * self.WR, 180 * self.HR), 32)
        self.draw_circle("#7E6D4B", 136 * self.WR, 148 * self.HR, 65)

    def draw_mission_panel(self):
        self.draw_rect("#FF0000", (0, 264 * self.HR, self.WIDTH, 680 * self.HR))

    ##################
    #     BUTTON     #
    ##################
    def draw_buttons(self):
        self.button_back.draw()
        self.button_next.draw()
        self.button_add.draw()
        self.button_reset.draw()

    def add_button_pressed(self, event):
        return self.button_add.is_clicked(event)

    def reset_button_pressed(self, event):
        return self.button_reset.is_clicked(event)

    def back_button_pressed(self, event):
        return self.button_back.is_clicked(event)

    def next_button_pressed(self, event):
        return self.button_next.is_clicked(event)

    ##################
    #      MENU      #
    ##################
    def init_buttons(self):
        # temp buttons
        baseline = self.HR * (264 + 680)
        init_x = self.WIDTH / 2
        button_color = "#EDEDED"
        font_color = "#FFB435"

        self.button_back = self.create_button(button_color, init_x - 120, baseline + 68 * self.HR, "<", font_color)
        self.button_add = self.create_button(button_color, init_x + 40, baseline + 68 * self.HR, "+", font_color)
        self.button_reset = self.create_button(button_color, init_x - 40, baseline + 68 * self.HR, "R", font_color, 48)
        self.button_next = self.create_button(button_color, init_x + 120, baseline + 68 * self.HR, ">", font_color)

    def draw_menu(self):
        self.draw_background()
        self.draw_progress_bar()
        self.draw_mission_panel()
        self.draw_buttons()



