import os

while True:
    # Get input from user
    user_input = input(f"{os.getcwd()} $ ")

    # Handle exit command
    if user_input == "exit":
        break

    # Parse command and arguments
    command, *args = user_input.split()
import readline

# Set up history file and enable command history
history_file = ".my_shell_history"
readline.read_history_file(history_file)
readline.set_history_length(1000)

# Define function for retrieving previous command
def get_previous_command():
    current_history_len = readline.get_current_history_length()
    if current_history_len > 1:
        previous_command = readline.get_history_item(current_history_len - 2)
        return previous_command.strip()
    else:
        return ""

# Main loop
while True:
    # Get user input
    user_input = input("my_shell> ")

    # Handle arrow up to get previous command
    if user_input == "\033[A":
        previous_command = get_previous_command()
        print(previous_command)
        user_input = previous_command

    # Exit on Ctrl-D
    if not user_input:
        break

    # Do something with user input
    print("You entered:", user_input)

    # Add input to history
    readline.add_history(user_input)

# Save history file
readline.write_history_file(history_file)

    # Execute command
    if command == "cd":
        # Handle changing directory
        try:
            os.chdir(args[0])
        except FileNotFoundError:
            print(f"Directory not found: {args[0]}")
        except IndexError:
            print("No directory specified")
    else:
        # Execute other commands using os.system
        os.system(user_input)
