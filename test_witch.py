import unittest
from witch import mainProgram

class witchTest(unittest.TestCase):
    def test_witch(self):
        self.assertEqual(mainProgram('A',10,12,'B',13,17),4.2)
        self.assertEqual(mainProgram('A',10,12,'B',13,17),4.5)
        

if __name__ == '__main__':
    unittest.main()