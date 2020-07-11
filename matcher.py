import re
import os


class Matcher:

    @staticmethod
    def match(path, pattern):
        matches = []
        search_pattern = re.compile(r'{}'.format(pattern))
        for file in os.listdir(path):
            mo = search_pattern.search(file)
            if mo is not None:
                matches.append(file)
        return matches

    @staticmethod
    def match_multiple(path, patterns: dict):
        matches = []
        for file in os.listdir(path):
            hits = []
            for pattern in patterns:
                search_pattern = re.compile(r'{}'.format(pattern))
                mo = search_pattern.search(file)
                if mo is not None:
                    hits.append(pattern)
            matches.append((file, hits))
        return matches
