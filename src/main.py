
"""
1. Provision to add missions
2. Provision to mark missions as complete
3. Provision to save missions via files
4. Provision to reset mission progress
5. Provision to delete missions
6. Provision to load mission data from files
"""

import pygame as pg
import math
from mission_manager import MissionManager
from surface_manager import SurfaceManager

data_path = "data.txt"
pg.init()

if __name__ == "__main__":
    mm = MissionManager()
    screen = SurfaceManager()

    #load mission data
    mm.update_missions(data_path)

    # initialize variables
    program_running = True
    CARDS = len(mm.missions)
    MAX_CARDS = 4
    card_count = CARDS % MAX_CARDS
    card_index = -1
    page = 1

    while program_running:
        ####################
        #  EVENT HANDLING  #
        ####################
        mm.update_missions(data_path)
        for event in pg.event.get():
            # Check close program
            if event.type == pg.QUIT:
                program_running = False
                break

            #Menu events
            if screen.next_button_pressed(event):
                print("next")
                page = min(math.ceil(CARDS / MAX_CARDS), page + 1)

            if screen.back_button_pressed(event):
                print("back")
                page = max(1, page - 1)

            if screen.reset_button_pressed(event):
                print("reset")
                page = 1

            if screen.add_button_pressed(event):
                print("add")

            index_button = screen.index_button_pressed(event)
            if index_button:
                card_index = 4 * (page - 1) + index_button - 1
                print(card_index)

        ####################
        #  LOGIC HANDLING  #
        ####################
        if card_index > -1:
            mm.missions[card_index].is_done = True

        #reset variables
        card_count = min(max(CARDS - (page - 1) * 4, 0), 4)
        card_index = -1

        #update file
        mm.update_file(data_path)

        ####################
        # DISPLAY HANDLING #
        ####################
        # Draw Menu
        screen.draw_menu(card_count, page)

        # Update display
        pg.display.update()

    pg.quit()



