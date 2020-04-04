import unittest
from lab import count


class TestLab4(unittest.TestCase):
    def testADJ(self):
        self.assertEqual(count('Зеленый, красная, одиннадцать.'), (2, 0, 0))

    def testADVERB(self):
        self.assertEqual(count('Вблизи, хорошо, вчера, слишком, сослепу, нарочно, наречие'), (0, 6, 0))

    def testVERB(self):
        self.assertEqual(count('Плыла, думал, думать, да.'), (0, 0, 3))

    def testText(self):
        with open('text.txt', 'r') as f:
            text = f.read()
            self.assertEqual(count(text), (314, 7, 10))
            
if __name__ == '__main__':
    unittest.main()
