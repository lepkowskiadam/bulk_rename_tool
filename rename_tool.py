from snapshot import Snapshot
from matcher import Matcher
import os


class RenameTool:
    def __init__(self):
        self.matcher = Matcher()
        self.snapshot = Snapshot()

    def replace(self, path, **kwargs):
        matches = self.matcher.match(path, **kwargs)
        old_file_names = []
        new_file_names = []
        for file, hits in matches:
            ext = '.' + file.rsplit('.')[-1]
            new_file = file
            for hit in hits:
                new_file = new_file.replace(hit, kwargs[hit])
            new_file = new_file[:-len(ext)] + ext
            old_file_names.append(file)
            new_file_names.append(new_file)
            os.rename(dst=os.path.join(path, new_file), src=os.path.join(path, file))
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

    def rename(self, path, **kwargs):
        matches = self.matcher.match(path, **kwargs)
        old_file_names = []
        new_file_names = []
        for num, file in enumerate(matches):
            if file[1]:
                ext = '.' + file[0].rsplit('.')[-1]
                new = kwargs[file[1][0]] + f'_{num}' + ext
                old_file_names.append(file[0])
                new_file_names.append(new)
                os.rename(dst=os.path.join(path, new), src=os.path.join(path, file[0]))
        self.snapshot.save_state(path, old_file_names, new_file_names)
        return new_file_names
