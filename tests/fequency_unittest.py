import sys
sys.path.insert(0, '../')
from freq_analysis import ArgumentParser, Instance
from frequency import frequency
from collections import Counter
import unittest

class FrequencyTest(unittest.TestCase):
    def setUp(self):
        c = Counter()
        c.update('The quick brown fox jumped over the lazy dog.')
        self.key_length_one_dist = [c]
        c1 = Counter()
        c1.update('T i o xueorhlyo')
        c2 = Counter()
        c2.update('hqcbwf mdv ea g')
        c3 = Counter()
        c3.update('eukrnojp et zd.')
        self.key_length_three_dist = [c1, c2, c3]
        self.parser = ArgumentParser()
    
    def test_frequency_key_length_one(self):
        self.parser.set_args(['read', '-s', 'The quick brown fox jumped over the lazy dog.'])
        self.parser.run_cmd()
        self.parser.set_args(['frequency'])
        self.assertEquals(self.parser.run_cmd()[0] - self.key_length_one_dist[0],
                          Counter())
    
    def test_frequency_key_length_three(self):
        self.parser.set_args(['read', '-s', 'The quick brown fox jumped over the lazy dog.'])
        self.parser.run_cmd()
        self.parser.set_args(['frequency', '-kl', '3'])
        dist_list = self.parser.run_cmd()
        for x in range(len(dist_list)):
            self.assertEquals(dist_list[x] - self.key_length_three_dist[x], Counter())

if __name__ == '__main__':
    unittest.main()