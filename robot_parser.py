COMMANDS = {
    "0X123": "moveForward",
    "0X789": "moveBackward",
    "0XABC": "stop",
}

def parse(stream):
    commands = []
    for token in stream.split():
        code, _, count = token.partition("*")
        commands += [COMMANDS[code]] * int(count or 1)
    return commands