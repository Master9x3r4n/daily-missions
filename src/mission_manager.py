
from mission import Mission

class MissionManager:
    def __init__(self):
        self.missions: list[Mission] = []

    def add_mission(self, name: str, desc: str):
        self.missions.append(Mission(name, desc))

    def search_mission_name(self, name: str):
        for m in self.missions:
            if m.name == name:
                print(f"Found mission name: {m.name}")
                return m
        print(f"Mission name {name} not found")
        return None

    def delete_mission(self, name: str):
        m = self.search_mission_name(name)
        if m:
            self.missions.remove(m)
        else:
            print(f"Failed to delete mission {name}")

    def print_missions(self):
        for m in self.missions:
            print(f"'{m.name}': {m.description}")
