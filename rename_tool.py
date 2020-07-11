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
            ext = '.' + file.rsplit('.')[-1]
            new = file.replace(pattern, new_pattern)[:-len(ext)] + ext
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

    def display_changes(self, path, pattern, new_pattern):
        to_update = self.matcher.match(path, pattern)
        updated = []
        for file in to_update:
            ext = '.' + file.rsplit('.')[-1]
            new = file.replace(pattern, new_pattern)[:-len(ext)] + ext
            updated.append(new)
        return zip(to_update, updated)

    def rename_full(self, path, pattern, new_pattern):
        to_update = self.matcher.match(path, pattern)
        updated = []
        for num, file in enumerate(to_update):
            ext = '.' + file.rsplit('.')[-1]
            new = new_pattern + f'_{num}' + ext
            updated.append(new)
            os.rename(dst=os.path.join(path, new), src=os.path.join(path, file))
        self.snapshot.save_state(path, pattern, new_pattern)
        return updated
