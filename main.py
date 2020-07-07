from rename_tool import RenameTool
from user_msg import UserMessage


def main():
    rename_tool = RenameTool()
    msg = UserMessage()
    command = ''
    while command != 'q':
        command = msg.prompt()
        if command.lower() == 'rename':
            try:
                path, pattern, new_pattern = msg.rename()
                changes_list = rename_tool.display_changes(path, pattern, new_pattern)
                if msg.display_changes(changes_list):
                    rename_tool.rename(path, pattern, new_pattern)
            except TypeError:
                pass
        else:
            try:
                if getattr(msg, command)():
                    getattr(rename_tool, command)()
            except AttributeError:
                msg.command_not_found(command)


if __name__ == '__main__':
    main()
