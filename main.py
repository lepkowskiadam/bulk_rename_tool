from rename_tool import RenameTool
from user_msg import UserMessage


def main():
    rename_tool = RenameTool()
    msg = UserMessage()
    command = ''
    while command != 'q':
        command = msg.prompt()
        if hasattr(rename_tool, command):
            if command == 'rename' or command == 'replace':
                try:
                    path, patterns = getattr(msg, command)()
                    getattr(rename_tool, command)(path, **patterns)
                except TypeError:
                    print('Path does not exist')
            else:
                if getattr(msg, command)():
                    getattr(rename_tool, command)()
        else:
            msg.command_not_found(command)


if __name__ == '__main__':
    main()
