import unittest
from slot_machine import slot_machine

class SlotMachineTest(unittest.TestCase):
    def test_three_cherries(self):
        self.assertEqual(slot_machine(10, ["cherry", "cherry", "cherry"]), 100)

    def test_three_lemons(self):
        self.assertEqual(slot_machine(5, ["lemon", "lemon", "lemon"]), 25)

    def test_three_oranges(self):
        self.assertEqual(slot_machine(2, ["orange", "orange", "orange"]), 6)

    def test_two_cherries_one_lemon(self):
        self.assertEqual(slot_machine(3, ["cherry", "cherry", "lemon"]), 6)

    def test_two_lemons_one_cherry(self):
        self.assertEqual(slot_machine(4, ["lemon", "lemon", "cherry"]), 4)

    def test_two_oranges_one_cherry(self):
        self.assertEqual(slot_machine(1, ["orange", "orange", "cherry"]), 1)
if __name__ == "__main__":
    unittest.main()