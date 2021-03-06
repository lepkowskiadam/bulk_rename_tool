from snapshot import Snapshot
from matcher import Matcher
import os


class RenameTool:
    def __init__(self):
        self.matcher = Matcher()
        self.snapshot = Snapshot()

    def replace(self, path, **kwargs):
        matches = self.matcher.match(path, **kwargs)
        old_file_names = [filename[0] for filename in matches]
        new_file_names = []
        for file, hits in matches:
            extension = '.' + file.rsplit('.')[-1]
            new_file = file
            for hit in hits:
                new_file = new_file.replace(hit, kwargs[hit])
            new_file = new_file[:-len(extension)] + extension
            new_file_names.append(new_file)
            os.rename(src=os.path.join(path, file), dst=os.path.join(path, new_file))
        self.snapshot.save_state(path, old_file_names, new_file_names)
        return new_file_names

    def undo(self):
        self.snapshot.undo()
        if self.snapshot.state == 0:
            path, new_file_names, old_file_names = self.snapshot.return_state()
        else:
            path, old_file_names, new_file_names = self.snapshot.return_state()
        for old, new in zip(old_file_names, new_file_names):
            os.rename(src=os.path.join(path, old), dst=os.path.join(path, new))
        return new_file_names

    def redo(self):
        self.snapshot.redo()
        path, old_file_names, new_file_names = self.snapshot.return_state()
        for old, new in zip(old_file_names, new_file_names):
            os.rename(src=os.path.join(path, old), dst=os.path.join(path, new))
        return new_file_names

    def rename(self, path, **kwargs):
        matches = self.matcher.match(path, **kwargs)
        old_file_names = [filename[0] for filename in matches]
        new_file_names = []
        for num, file in enumerate(matches):
            if file[1]:
                extension = '.' + file[0].rsplit('.')[-1]
                new = kwargs[file[1][0]] + f'_{num}' + extension
                new_file_names.append(new)
                os.rename(src=os.path.join(path, file[0]), dst=os.path.join(path, new))
        self.snapshot.save_state(path, old_file_names, new_file_names)
        return new_file_names
