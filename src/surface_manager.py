import pygame as pg
from button import Button
from mission_manager import Mission

pg.init()
pg.font.init()

TITLE_LIMIT = 16
DESC_LIMIT = 200

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

    #These two functions of wrap_text were vibecoded
    def wrap_text(self, text, font, max_width):
        words = text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line.rstrip())
                current_line = word + " "

        if current_line:
            lines.append(current_line.rstrip())

        return lines

    def draw_text_wrapped(self, text, font, color, rect, line_spacing=2):
        x, y, width, height = rect
        lines = self.wrap_text(text, font, width)

        line_height = font.get_height()
        for line in lines:
            self.SURFACE.blit(font.render(line, True, color), (x, y))
            y += line_height + line_spacing
            if y > rect[1] + height:
                break

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

    def draw_progress_bar(self, missions, completed):
        #progress bar
        progress = completed / len(missions)
        offset = 16
        self.draw_rect("#FFFFFF", (136 * self.WR, 58 * self.HR, 1760 * self.WR, 180 * self.HR), 32)
        self.draw_rect("#B4B4B4", (136 * self.WR, 58 * self.HR + offset, 1760 * self.WR - 16, 180 * self.HR -offset * 2), 32)
        self.draw_rect("#FFB435", (136 * self.WR, 58 * self.HR + offset * 2,
                                   (1760 * self.WR - 32) * progress, 180 * self.HR - offset * 4), 32)

        self.draw_circle("#7E6D4B", 136 * self.WR, 148 * self.HR, 65)


    def draw_mission_panel(self, card_count = 4, page = 1, missions: list[Mission] = None):
        base_y = 264 * self.HR

        #bg for reference
        #self.draw_rect("#FF0000", (0, base_y, self.WIDTH, 680 * self.HR))

        #display cards
        for i in range(card_count):
            card_color = "#F2EFEF"
            card_index = 4 * (page - 1) + i

            #Draw card and card text area
            self.draw_rect(card_color, (11 + 285 * i, base_y + 8, 275, 392), border_radius=32)
            self.draw_rect("#FFFFFF", (11 + 285 * i + 16, base_y + 8 + 16, 275 - 32, 392 - 104))

            #Draw mission text
            if missions:
                title_font = pg.font.SysFont("Arial", 32, bold = True)
                desc_font = pg.font.SysFont("Arial", 24)
                font_color = "#000000" if not missions[card_index].is_done else "#FFB435"

                title_text = missions[card_index].name[:TITLE_LIMIT]
                desc_text = missions[card_index].description[:DESC_LIMIT]

                self.draw_text_wrapped(title_text, title_font, font_color,
                                       (11 + 285 * i + 24, base_y + 8 + 16, 275 - 32, 392 - 104))

                self.draw_text_wrapped(desc_text, desc_font, font_color,
                                       (11 + 285 * i + 24, base_y + 8 + 52, 275 - 32, 392 - 104))

            #Draw card buttons
            self.draw_circle("#AAFFAA", 11 + 285 * i + 275 - 48, base_y + 400 - 48, 32)
            self.draw_circle("#FFFFFF", 11 + 285 * i + 275 - 48, base_y + 400 - 48, 16)

            if missions and not missions[card_index].is_done:
                self.draw_button_index(i+1)
                self.draw_circle("#FFB435", 11 + 285 * i + 275 - 48, base_y + 400 - 48, 16)

    ##################
    #      MENU      #
    ##################
    def draw_menu(self, card_count = 4, page = 1, missions = None, completed = 0):
        self.draw_background()
        self.draw_progress_bar(missions, completed)
        self.draw_mission_panel(card_count, page, missions)
        self.draw_menu_buttons()



