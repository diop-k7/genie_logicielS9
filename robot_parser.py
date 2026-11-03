
from enum import Enum


class Command(Enum):
    MOVE_FORWARD = "moveForward"
    MOVE_BACKWARD = "moveBackward"
    STOP = "stop"

COMMANDS = {
    "0X123": Command.MOVE_FORWARD,
    "0X789": Command.MOVE_BACKWARD,
    "0XABC": Command.STOP,
}

def parse(stream):
    commands = []
    for token in stream.split():
        code, _, count = token.partition("*")
        commands += [COMMANDS[code]] * int(count or 1)
    return commands