import pygame as pg

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

    def draw_button (self, button_color, x, y, text = "", font_color = "#000000", font_size = 64):
        c = self.draw_circle(button_color, x, y, 32)

        # set the font style
        font = pg.font.SysFont("Arial", font_size)

        # create surface text
        txt_surface = font.render(text, True, font_color)

        # add the text to the surface
        txt_rect = txt_surface.get_rect(center=c.center)

        # blit the text onto to the surface
        self.SURFACE.blit(txt_surface, txt_rect)

        def is_clicked(event):
            # get mouse click
            if event.type == pg.MOUSEBUTTONDOWN:
                if c.collidepoint(event.pos):
                    return True
            return False

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
    #      MENU      #
    ##################
    def draw_menu(self):
        self.draw_background()
        self.draw_progress_bar()
        self.draw_mission_panel()

        #temp buttons
        baseline = self.HR * (264 + 680)
        init_x = self.WIDTH / 2
        self.draw_button("#FFFFFF", init_x + 40, baseline + 68 * self.HR, "+")
        self.draw_button("#FFFFFF", init_x + 120, baseline + 68 * self.HR, ">")
        self.draw_button("#FFFFFF", init_x - 40, baseline + 68 * self.HR, "R", font_size= 48)
        self.draw_button("#FFFFFF", init_x - 120, baseline + 68 * self.HR, "<")