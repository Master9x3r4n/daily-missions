
from mission import Mission

class MissionManager:
    def __init__(self):
        self.missions: list[Mission] = []

    def add_mission(self, name: str, desc: str, is_done: bool = False):
        self.missions.append(Mission(name, desc, is_done))

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

    def get_progress(self):
        count = 0
        for m in self.missions:
            if m.is_done: count += 1
        return count

    def update_file(self, file_path: str):
        with open(file_path, "w") as file:
            for m in self.missions:
                file.write(m.name+"\n")
                file.write(m.description+"\n")
                file.write(str(m.is_done)+"\n")

    def update_missions(self, file_path: str):
        with open(file_path, "r") as file:
            c = file.readlines()

        self.missions = []
        for i in range(0, len(c), 3):
            self.add_mission(c[i].strip(), c[i+1].strip(), c[i+2].strip() == "True")
