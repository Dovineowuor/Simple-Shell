import os

while True:
    # Get input from user
    user_input = input(f"{os.getcwd()} $ ")

    # Handle exit command
    if user_input == "exit":
        break

    # Parse command and arguments
    command, *args = user_input.split()

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
