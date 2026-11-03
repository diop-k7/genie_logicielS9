import unittest
from robot_parser import parse

class RobotParserTest(unittest.TestCase):
    def test_0x123_is_move_forward(self):
        self.assertEqual(parse("0X123"), ["moveForward"])

    def test_0x789_is_move_backward(self):
        self.assertEqual(parse("0X789"), ["moveBackward"])

    def test_0xABC_is_stop(self):
        self.assertEqual(parse("0XABC"), ["stop"])
        
    def test_stream_of_several_commands(self):
        self.assertEqual(
            parse("0X123 0X789 0XABC"),
            ["moveForward", "moveBackward", "stop"],
        )
if __name__ == "__main__":
    unittest.main()