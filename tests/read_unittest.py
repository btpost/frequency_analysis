import sys
sys.path.insert(0, '../')
from freq_analysis import ArgumentParser, Instance
from read import reader
import unittest

class ReadTest(unittest.TestCase):
    def setUp(self):
        self.text_file = open("test_text_file.txt", 'r').read()
        self.testing_string = 'Testing String'
        self.parser = ArgumentParser()

    def test_read_text_file(self):
        self.assertEquals(reader(["test_text_file.txt"]), self.text_file)

    def test_read_string(self):
        self.assertEquals(reader(['-s', 'Testing String']), self.testing_string)
    
    def test_read_into_instance(self):
        self.parser.get_args(['read', '-s', 'This is test text'])
        self.parser.run_cmd()
        self.assertEqual(self.parser.instance.original_text, 'This is test text')

    def test_read_into_instance_from_file(self):
        self.parser.get_args(['read', 'test_text_file.txt'])
        self.parser.run_cmd()
        self.assertEqual(self.parser.instance.original_text, 'This is a text file to test the read method')


if __name__ == '__main__':
    unittest.main()
