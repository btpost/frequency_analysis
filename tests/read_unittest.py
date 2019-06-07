import sys
sys.path.insert(0, '../')
from freq_analysis import ArgumentParser
from read import reader
import unittest

class ReadTest(unittest.TestCase):
    def setUp(self):
        self.text_file = open("test_text_file.txt", 'r').read()
        self.testing_string = 'Testing String'

    def test_read_text_file(self):
        self.assertEquals(reader(["test_text_file.txt"]).read(), self.text_file)

    def test_read_string(self):
        self.assertEquals(reader(['-s', 'Testing String']), self.testing_string)
    
    self.parser.get_args(['read', '-s', 'This is test text'])
        self.parser.run_cmd()
        self.assertEqual(self.parser.instance.original_text, 'This is test text')


if __name__ == '__main__':
    unittest.main()
