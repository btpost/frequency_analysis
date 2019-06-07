import sys
sys.path.insert(0, '../')
from freq_analysis import ArgumentParser
import unittest


class TestArgumentParser(unittest.TestCase):
    def setUp(self):
        self.parser = ArgumentParser()

    def test_read(self):
        self.parser.get_args(['read'])
        self.assertEqual(self.parser.run_cmd(), 'running read')

    def test_print(self):
        self.parser.get_args(['print'])
        self.assertEqual(self.parser.run_cmd(), 'running print')

    def test_set(self):
        self.parser.get_args(['set'])
        self.assertEqual(self.parser.run_cmd(), 'running set')

    def test_reset(self):
        self.parser.get_args(['reset'])
        self.assertEqual(self.parser.run_cmd(), 'running reset')

    def test_frequency(self):
        self.parser.get_args(['frequency'])
        self.assertEqual(self.parser.run_cmd(), 'running frequency')

    def test_apply_key(self):
        self.parser.get_args(['apply_key'])
        self.assertEqual(self.parser.run_cmd(), 'running apply_key')

    def tearDown(self):
        del self.parser

if __name__ == '__main__':
    unittest.main()
