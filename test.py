import unittest
from Bulba import Bulba

class MyTestCase(unittest.TestCase):
    def test_Bulba_attack(self):
        bulba = Bulba()
        self.assertEqual(bulba.attack(), "Bulba attack ur mind ♂")  # add assertion here


if __name__ == '__main__':
    unittest.main()
