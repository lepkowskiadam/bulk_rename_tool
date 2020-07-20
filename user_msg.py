import os


class UserMessage:

    @staticmethod
    def replace():
        path = input('Enter directory path: ')
        old_new = dict()
        if os.path.exists(path):
            patterns = input('Enter patterns to be replaced (separate them using ","): ')
            new_patterns = input('Enter new patterns in the same order: ')
            patterns = patterns.split(', ')
            new_patterns = new_patterns.split(', ')
            if len(patterns) == len(new_patterns):
                for old, new in zip(patterns, new_patterns):
                    old_new[old] = new
                return path, old_new
            else:
                print('The number of patterns don\'t match')

    @staticmethod
    def undo():
        command = input('Do you wish to undo the recent changes? [y/n]: ')
        if command.lower() == 'y':
            return True
        return False

    @staticmethod
    def redo():
        command = input('Do you wish to redo the recent changes? [y/n]: ')
        if command.lower() == 'y':
            return True
        return False

    @staticmethod
    def command_not_found(command):
        if command.lower() != 'q':
            print('Command not found, try again')

    @staticmethod
    def prompt():
        print('Enter "q" to quit')
        command = input('Available options: replace/rename/undo/redo: ')
        return command.lower()

    @staticmethod
    def rename():
        path = input('Enter directory path: ')
        if os.path.exists(path):
            pattern = input('Enter pattern to be replaced: ')
            new_pattern = input('Enter new pattern: ')
            patterns = {pattern: new_pattern}
            return path, patterns
