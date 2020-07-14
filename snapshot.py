class Snapshot:
    def __init__(self):
        self.states = []
        self.state = -1

    def save_state(self, path, old_file_names: list, new_file_names: list):
        if self.state != len(self.states) - 1:
            self.states = self.states[:self.state + 1]
        self.states.append((path, old_file_names, new_file_names))
        self.state += 1

    def return_state(self):
        return self.states[self.state]

    def undo(self):
        if self.state > 0:
            self.state -= 1

    def redo(self):
        if self.state < len(self.states) - 1:
            self.state += 1
