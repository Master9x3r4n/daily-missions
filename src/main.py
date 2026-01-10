
"""
1. Provision to add missions
2. Provision to mark missions as complete
3. Provision to save missions via files
4. Provision to reset mission progress
5. Provision to delete missions
6. Provision to load mission data from files
"""

import pygame as pg
from mission_manager import MissionManager
from surface_manager import SurfaceManager

data_path = "data.txt"
pg.init()

if __name__ == "__main__":
    mm = MissionManager()
    screen = SurfaceManager()

    program_running = True
    while program_running:
        # Event handling
        for event in pg.event.get():
            # Check close program
            if event.type == pg.QUIT:
                program_running = False
                break

            #Menu events
            if screen.next_button_pressed(event):
                print("next")

            if screen.reset_button_pressed(event):
                print("reset")

            if screen.add_button_pressed(event):
                print("add")

            if screen.back_button_pressed(event):
                print("back")

        #Display events
        screen.draw_menu()


        pg.display.update()

    pg.quit()



