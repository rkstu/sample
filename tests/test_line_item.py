import unittest
import sys
# sys.path.insert(0, "C:\Users\91956\Desktop\sample")
sys.path.insert(0, 'C:/Users/91956/Desktop/sample')

from main import process_list

class TestProcessListFunction(unittest.TestCase):
    def test_valid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        result = process_list(input_list)
        self.assertEqual(result, [1, 5, 7, 11, 13, 17, 19])

    def test_invalid_length(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        with self.assertRaises(ValueError):
            process_list(input_list)

if __name__ == "__main__":
    unittest.main()
