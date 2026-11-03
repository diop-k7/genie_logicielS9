import unittest
from robot_parser import parse, Command

class RobotParserTest(unittest.TestCase):
    def test_0x123_is_move_forward(self):
        self.assertEqual(parse("0X123"), [Command.MOVE_FORWARD])

    def test_0x789_is_move_backward(self):
        self.assertEqual(parse("0X789"), [Command.MOVE_BACKWARD])

    def test_0xABC_is_stop(self):
        self.assertEqual(parse("0XABC"), [Command.STOP])

    def test_stream_of_several_commands(self):
        self.assertEqual(
            parse("0X123 0X789 0XABC"),
            [Command.MOVE_FORWARD, Command.MOVE_BACKWARD, Command.STOP],
        )

    def test_stream_with_repeated_commands(self):
        self.assertEqual(
            parse("0X123*3 0X789*2 0XABC"),
            [Command.MOVE_FORWARD, Command.MOVE_FORWARD, Command.MOVE_FORWARD, Command.MOVE_BACKWARD, Command.MOVE_BACKWARD, Command.STOP],
        )
if __name__ == "__main__":
    unittest.main()