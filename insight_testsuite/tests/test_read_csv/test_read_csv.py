#this script tests the functionality of the function read_csv

import unittest
import sys

#set current directory as src to import h1b_stats.py
sys.path.insert(0, '../../../src/')
import h1b_stats

class ReadCsvTestCase(unittest.TestCase):
    """Test read_csv function."""

    def test_read_csv(self):
        """Is csv file correctly read?"""
        #test data list
        data = [['row_number', 'col2', 'col3', 'col4'],
                ['row2', 'name2', '1.0', '2'],
                ['row3', 'name3', '3.0', '4'],
                ['row4', 'name4', '5.0', '6']]

        self.assertEqual(h1b_stats.read_csv('test_read_csv.csv'), data)

if __name__ == '__main__':
    unittest.main()
