class Snapshot:
    def __init__(self):
        self.states = []
        self._i = -1

    def save_state(self, path, pattern, new_pattern):
        self.states.append((path, pattern, new_pattern))
