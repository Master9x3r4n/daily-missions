
"""
1. Provision to add missions
2. Provision to mark missions as complete
3. Provision to save missions via files
4. Provision to reset mission progress
5. Provision to delete missions
6. Provision to load mission data from files
"""

from mission_manager import MissionManager

if __name__ == "__main__":
    mm = MissionManager()
    mm.add_mission("Walker", "Take a long walk")
    mm.print_missions()
    mm.delete_mission("Walker")
    mm.print_missions()