from snapshot import Snapshot
from matcher import Matcher
import os


class RenameTool:
    def __init__(self):
        self.matcher = Matcher()
        self.snapshot = Snapshot()

    def rename(self, path, pattern, new_pattern):
        old_file_names = self.matcher.match(path, pattern)
        new_file_names = []
        for file in old_file_names:
            ext = '.' + file.rsplit('.')[-1]
            new = file.replace(pattern, new_pattern)[:-len(ext)] + ext
            new_file_names.append(new)
            os.rename(dst=os.path.join(path, new), src=os.path.join(path, file))
        self.snapshot.save_state(path, old_file_names, new_file_names)
        return new_file_names

    def undo(self):
        self.snapshot.undo()
        path, new_file_names, old_file_names = self.snapshot.return_state()
        for new, old in zip(new_file_names, old_file_names):
            os.rename(dst=os.path.join(path, new), src=os.path.join(path, old))
        return new_file_names

    def redo(self):
        self.snapshot.redo()
        path, old_file_names, new_file_names = self.snapshot.return_state()
        for new, old in zip(new_file_names, old_file_names):
            os.rename(dst=os.path.join(path, new), src=os.path.join(path, old))
        return new_file_names

    def display_changes(self, path, pattern, new_pattern):
        old_file_names = self.matcher.match(path, pattern)
        new_file_names = []
        for file in old_file_names:
            ext = '.' + file.rsplit('.')[-1]
            new = file.replace(pattern, new_pattern)[:-len(ext)] + ext
            new_file_names.append(new)
        return zip(old_file_names, new_file_names)

    def rename_full(self, path, pattern, new_pattern):
        old_file_names = self.matcher.match(path, pattern)
        new_file_names = []
        for num, file in enumerate(old_file_names):
            ext = '.' + file.rsplit('.')[-1]
            new = new_pattern + f'_{num}' + ext
            new_file_names.append(new)
            os.rename(dst=os.path.join(path, new), src=os.path.join(path, file))
        self.snapshot.save_state(path, old_file_names, new_file_names)
        return new_file_names

    def rename_multiple(self, path, **kwargs):
        old_file_names = self.matcher.match_multiple(path, **kwargs)
        updated = []
        for file, hits in old_file_names:
            ext = '.' + file.rsplit('.')[-1]
            new_file = file
            for hit in hits:
                new_file = new_file.replace(hit, kwargs[hit])
            new_file = new_file[:-len(ext)] + ext
            updated.append(new_file)
            os.rename(dst=os.path.join(path, new_file), src=os.path.join(path, file))
        return updated
