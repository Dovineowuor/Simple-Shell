# this function uses the arrow up keyboard function to read the previous command history
import readline

# Use the GNU readline library to enable arrow key handling
readline.parse_and_bind('"\e[A": history-search-backward')

def arrow_up():
    # Get the previous command from the readline history
    command = readline.get_history_item(readline.get_current_history_length() - 1)

    # If there's no previous command, return an empty string
    if command is None:
        return ''

    # Otherwise, return the previous command with the newline stripped
    return command.strip('\n')
