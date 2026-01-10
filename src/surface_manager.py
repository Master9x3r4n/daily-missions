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

        # Initialize buttons
        self.button_back: Button = None
        self.button_add: Button = None
        self.button_reset: Button = None
        self.button_next: Button = None
        self.button_index1: Button = None
        self.button_index2: Button = None
        self.button_index3: Button = None
        self.button_index4: Button = None
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
    #     BUTTON     #
    ##################
    def init_buttons(self):
        # menu buttons
        baseline = self.HR * (264 + 680)
        init_x = self.WIDTH / 2
        button_color = "#EDEDED"
        font_color = "#FFB435"

        self.button_back = self.create_button(button_color, init_x - 120, baseline + 68 * self.HR, "<", font_color)
        self.button_add = self.create_button(button_color, init_x + 40, baseline + 68 * self.HR, "+", font_color)
        self.button_reset = self.create_button(button_color, init_x - 40, baseline + 68 * self.HR, "R", font_color,
                                               48)
        self.button_next = self.create_button(button_color, init_x + 120, baseline + 68 * self.HR, ">", font_color)

        # index buttons
        base_y = 264 * self.HR
        button_color = "#7E6D4B"
        self.button_index1 = self.create_button(button_color, 11 + 285 * 0 + 275 - 48, base_y + 352, "+", font_color, 48)
        self.button_index2 = self.create_button(button_color, 11 + 285 * 1 + 275 - 48, base_y + 352, "+", font_color, 48)
        self.button_index3 = self.create_button(button_color, 11 + 285 * 2 + 275 - 48, base_y + 352, "+", font_color, 48)
        self.button_index4 = self.create_button(button_color, 11 + 285 * 3 + 275 - 48, base_y + 352, "+", font_color, 48)

    def draw_menu_buttons(self):
        self.button_back.draw()
        self.button_next.draw()
        self.button_add.draw()
        self.button_reset.draw()

    def draw_button_index(self, index):
        if index == 1:
            self.button_index1.draw()
        elif index == 2:
            self.button_index2.draw()
        elif index == 3:
            self.button_index3.draw()
        elif index == 4:
            self.button_index4.draw()

    def add_button_pressed(self, event):
        return self.button_add.is_clicked(event)

    def reset_button_pressed(self, event):
        return self.button_reset.is_clicked(event)

    def back_button_pressed(self, event):
        return self.button_back.is_clicked(event)

    def next_button_pressed(self, event):
        return self.button_next.is_clicked(event)

    def index_button_pressed(self, event):
        if self.button_index1.is_clicked(event):
            return 1
        elif self.button_index2.is_clicked(event):
            return 2
        elif self.button_index3.is_clicked(event):
            return 3
        elif self.button_index4.is_clicked(event):
            return 4
        else:
            return 0

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

    def draw_mission_panel(self, card_count = 4, page = 1):
        base_y = 264 * self.HR

        #bg for reference
        #self.draw_rect("#FF0000", (0, base_y, self.WIDTH, 680 * self.HR))

        #display cards
        for i in range(card_count):
            card_color = "#F2EFEF"
            card_index = 4 * (page - 1) + i
            index_font = pg.font.SysFont("Arial", 32)

            #Draw card and card text area
            self.draw_rect(card_color, (11 + 285 * i, base_y + 8, 275, 392), border_radius=32)
            self.draw_rect("#FFFFFF", (11 + 285 * i + 16, base_y + 8 + 16, 275 - 32, 392 - 104))

            #Draw card buttons
            self.draw_circle("#AAFFAA", 11 + 285 * i + 275 - 48, base_y + 400 - 48, 32)
            self.draw_text(index_font, f"O", 11 + 285 * i + 275 - 58, base_y + 400 - 66)

            self.draw_button_index(i+1)

    ##################
    #      MENU      #
    ##################
    def draw_menu(self, card_count = 4, page = 1):
        self.draw_background()
        self.draw_progress_bar()
        self.draw_mission_panel(card_count, page)
        self.draw_menu_buttons()



