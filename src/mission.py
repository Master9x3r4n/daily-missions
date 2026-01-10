
class Mission:
    def __init__(self, name: str, description: str, is_done = False):
        self.name = name
        self.description = description
        self.is_done = is_done

    def complete(self):
        self.is_done = True