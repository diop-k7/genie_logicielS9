def parse(hexadecimal_command):
    # Convert the hexadecimal command to an integer
    command_int = int(hexadecimal_command, 16)

    # Define a mapping of command integers to their corresponding actions
    command_mapping = {
        0x123: ["moveForward"],
        0x456: ["turnLeft"],
        0x789: ["turnRight"],
        0xABC: ["stop"],
        # Add more mappings as needed
    }

    # Return the corresponding action for the given command, or an empty list if not found
    return command_mapping.get(command_int, [])