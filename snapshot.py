class Snapshot:
    def __init__(self):
        self.states = []
        self.state = -1

    def save_state(self, path, pattern, new_pattern):
        self.states.append((path, pattern, new_pattern))
        self.state += 1

    def return_state(self):
        return self.states[self.state]

    def undo(self):
        if self.state > 0:
            self.state -= 1
