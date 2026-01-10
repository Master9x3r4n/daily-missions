
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
from surface_manager import SurfaceManager, TITLE_LIMIT, DESC_LIMIT

data_path = "data.txt"
pg.init()

def add_mission(mm: MissionManager):
    print("###########################")
    print("#    ADD A NEW MISSION    #")
    print("###########################")
    name = input("Input new mission name (max 14 chars): ")
    if mm.search_mission_name(name, warn = False):
        print("ERROR: INVALID NAME. MISSION ALREADY EXISTS")
    else:
        desc = input("Input mission description (max 200 chars): ")
        mm.add_mission(name[:TITLE_LIMIT], desc[:DESC_LIMIT])

def delete_mission(mm: MissionManager):
    print("###########################")
    print("#    DELETE A MISSION     #")
    print("###########################")
    name = input("Input mission name exactly to delete: ")
    mm.delete_mission(name)

def edit_menu(mm: MissionManager):
    running = True
    while running:
        print("###########################")
        print("#      EDIT MISSIONS      #")
        print("###########################")
        print("What would you like to do?")
        print("[1] Add a new mission")
        print("[2] Delete an old mission")
        print("[*] Exit")
        choice = input("Input: ")
        if choice == "1":
            add_mission(mm)
        elif choice == "2":
            delete_mission(mm)
        else:
            running = False

def update(mm: MissionManager):
    mm.order_missions()
    mm.update_file(data_path)
    mm.update_missions(data_path)


if __name__ == "__main__":
    mm = MissionManager()
    screen = SurfaceManager()

    #load mission data
    mm.order_missions()
    mm.update_missions(data_path)
    update(mm)

    # initialize variables
    program_running = True
    MAX_CARDS = 4
    card_count = len(mm.missions) % MAX_CARDS
    card_index = -1
    page = 1

    while program_running:
        ####################
        #  EVENT HANDLING  #
        ####################
        for event in pg.event.get():
            # Check close program
            if event.type == pg.QUIT:
                program_running = False
                break

            #Menu events
            if screen.next_button_pressed(event):
                #print("next")
                page = min(math.ceil(len(mm.missions) / MAX_CARDS), page + 1)

            if screen.back_button_pressed(event):
                #print("back")
                page = max(1, page - 1)

            if screen.reset_button_pressed(event):
                #print("reset")
                mm.reset_missions()
                update(mm)

            if screen.add_button_pressed(event):
                edit_menu(mm)
                update(mm)

            index_button = screen.index_button_pressed(event)
            if index_button:
                card_index = 4 * (page - 1) + index_button - 1
                #print(card_index)

        ####################
        #  LOGIC HANDLING  #
        ####################
        if card_index > -1:
            mm.missions[card_index].is_done = True
            update(mm)

        #reset variables
        card_count = min(max(len(mm.missions) - (page - 1) * 4, 0), 4)
        card_index = -1

        ####################
        # DISPLAY HANDLING #
        ####################
        # Draw Menu
        screen.draw_menu(card_count, page, mm.missions, mm.get_progress())

        # Update display
        pg.display.update()

    pg.quit()



