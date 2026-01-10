
class Mission:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.is_done = False

    def complete(self):
        self.is_done = True