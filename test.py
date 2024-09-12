import unittest
from __init__ import FindAnyStrings, FindNotAnyStrings

class TestFindAnyStrings(unittest.TestCase):
    def test_run(self):
        string_list = ["tag1, tag2", "tag2, tag3", "tag3, tag4"]
        search_strings = ["tag2"]
        delimiter = [","]
        
        expected_indices = [0, 1]
        expected_strings = ["tag1, tag2", "tag2, tag3"]
        
        find_any_strings = FindAnyStrings()
        result_indices, result_strings = find_any_strings.run(string_list, search_strings, delimiter)
        
        self.assertEqual(result_indices, expected_indices)
        self.assertEqual(result_strings, expected_strings)

class TestFindNotAnyStrings(unittest.TestCase):
    def test_run(self):
        string_list = ["tag1, tag2", "tag2, tag3", "tag3, tag4"]
        search_strings = ["tag2"]
        delimiter = [","]
        
        expected_indices = [2]
        expected_strings = ["tag3, tag4"]
        
        find_not_any_strings = FindNotAnyStrings()
        result_indices, result_strings = find_not_any_strings.run(string_list, search_strings, delimiter)
        
        self.assertEqual(result_indices, expected_indices)
        self.assertEqual(result_strings, expected_strings)

if __name__ == '__main__':
    unittest.main()
