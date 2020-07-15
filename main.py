from rename_tool import RenameTool
from user_msg import UserMessage


def main():
    rename_tool = RenameTool()
    msg = UserMessage()
    command = ''
    while command != 'q':
        command = msg.prompt()
        if command.lower() == 'replace':
            path, patterns = msg.replace()
            rename_tool.replace(path, **patterns)
        else:
            try:
                if getattr(msg, command)():
                    getattr(rename_tool, command)()
            except AttributeError:
                msg.command_not_found(command)


if __name__ == '__main__':
    main()
