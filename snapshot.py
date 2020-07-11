class Snapshot:
    def __init__(self):
        self.states = []
        self.state = -1

    def save_state(self, path, pattern, new_pattern, func):
        if self.state != len(self.states) - 1:
            self.states = self.states[:self.state + 1]
        self.states.append((path, pattern, new_pattern, func))
        self.state += 1

    def return_state(self):
        return self.states[self.state]

    def undo(self):
        if self.state > 0:
            self.state -= 1

    def redo(self):
        if self.state < len(self.states) - 1:
            self.state += 1
