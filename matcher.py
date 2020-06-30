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
