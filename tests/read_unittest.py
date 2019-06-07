import sys
sys.path.insert(0, '../')
from freq_analysis import ArgumentParser
from read import read
import unittest

class ReadTest(unittest.TestCase):
    def setUp(self):
        self.text_file = open("text_file_test.txt", 'r')
        self.testing_string = 'Testing String'

    def test_read_text_file(self):
        self.assertEquals(read(["text_file_test.txt"]), self.text_file)

    def test_read_string(self):
        self.assertEquals(read(['-s', 'Testing String']), self.testing_string)


if __name__ == '__main__':
    unittest.main()
