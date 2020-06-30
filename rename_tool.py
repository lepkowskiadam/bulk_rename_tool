import os


class RenameTool:
    def __init__(self, matcher):
        self.matcher = matcher

    def rename(self, path, pattern, new_pattern):
        if os.path.exists(path):
            to_update = self.matcher.match(path, pattern)
            updated = []
            for file in to_update:
                new = file.replace(pattern, new_pattern)
                updated.append(new)
                os.rename(dst=os.path.join(path, new), src=os.path.join(path, file))
            return updated
