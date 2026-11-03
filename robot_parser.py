COMMANDS = {
    "0X123": "moveForward",
    "0X789": "moveBackward",
    "0XABC": "stop",
}

def parse(stream):
    return [COMMANDS[code] for code in stream.split()]