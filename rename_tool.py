from snapshot import Snapshot
from matcher import Matcher
import os


class RenameTool:
    def __init__(self):
        self.matcher = Matcher()
        self.snapshot = Snapshot()

    def rename(self, path, pattern, new_pattern):
        to_update = self.matcher.match(path, pattern)
        updated = []
        for file in to_update:
            new = file.replace(pattern, new_pattern)
            updated.append(new)
            os.rename(dst=os.path.join(path, new), src=os.path.join(path, file))
        self.snapshot.save_state(path, pattern, new_pattern)
        return updated

    def undo(self):
        self.snapshot.undo()
        path, new_pattern, old_pattern = self.snapshot.return_state()
        return self.rename(path, old_pattern, new_pattern)

    def redo(self):
        self.snapshot.redo()
        path, new_pattern, old_pattern = self.snapshot.return_state()
        return self.rename(path, old_pattern, new_pattern)
