import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from app.io.input import input_from_file_pandas, input_from_file

class TestInputFromFilePandas(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        self.test_data.to_json('test.json')
        
        self.test_data_hello = 'Hello, World!'
        with open('test.txt', 'w') as f:
            f.write(self.test_data_hello)

    def tearDown(self):
        import os
        if os.path.exists('test.json'):
            os.remove('test.json')
        if os.path.exists('test.txt'):
            os.remove('test.txt')

    def test_input_from_file_pandas_valid(self):
        result = input_from_file_pandas('test.json')
        assert_frame_equal(result, self.test_data)

    def test_input_from_file_pandas_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            input_from_file_pandas('nonexistent.json')

    def test_input_from_file_pandas_invalid(self):
        with open('test.json', 'w') as f:
            f.write('{"A": [1, 2, invalid], "B": [4, 5, 6]}')
        with self.assertRaises(ValueError):
            input_from_file_pandas('test.json')


    def test_input_from_file_valid(self):
        result = input_from_file('test.txt')
        self.assertEqual(result, self.test_data_hello)

    def test_input_from_file_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            input_from_file('nonexistent.txt')

    def test_input_from_file_empty(self):
        with open('test.txt', 'w') as f:
            f.write('')
        result = input_from_file('test.txt')
        self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()