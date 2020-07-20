import re
import os


class Matcher:

    @staticmethod
    def match(path, **kwargs):
        matches = []
        for file in os.listdir(path):
            hits = []
            for pattern in kwargs:
                search_pattern = re.compile(r'{}'.format(pattern))
                mo = search_pattern.search(file)
                if mo is not None:
                    hits.append(pattern)
            matches.append((file, hits))
        return matches
