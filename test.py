import unittest
from unittest.mock import patch
from __init__ import FindAnyStrings, FindNotAnyStrings, RandomNormalDist, FilterStringListByIndexList, StringToIndex

class TestStringToIndex(unittest.TestCase):
    def test_run_with_comma_delimiter(self):
        string_to_index = StringToIndex()
        string = "1,2,3,4,5"
        delimiter = ","
        expected_output = ([1, 2, 3, 4, 5],)
        actual_output = string_to_index.run(string, delimiter)
        self.assertEqual(actual_output, expected_output)

    def test_run_with_space_delimiter(self):
        string_to_index = StringToIndex()
        string = "1 2 3 4 5"
        delimiter = " "
        expected_output = ([1, 2, 3, 4, 5],)
        actual_output = string_to_index.run(string, delimiter)
        self.assertEqual(actual_output, expected_output)

    def test_run_with_semicolon_delimiter(self):
        string_to_index = StringToIndex()
        string = "1;2;3;4;5"
        delimiter = ";"
        expected_output = ([1, 2, 3, 4, 5],)
        actual_output = string_to_index.run(string, delimiter)
        self.assertEqual(actual_output, expected_output)

    def test_run_with_empty_string(self):
        string_to_index = StringToIndex()
        string = ""
        delimiter = ","
        with self.assertRaises(ValueError):
            string_to_index.run(string, delimiter)

    def test_run_with_non_numeric_values(self):
        string_to_index = StringToIndex()
        string = "a,b,c"
        delimiter = ","
        with self.assertRaises(ValueError):
            string_to_index.run(string, delimiter)

class TestFilterStringListByIndexList(unittest.TestCase):
    def test_run(self):
        string_list = ["apple", "banana", "cherry", "date"]
        index_list = [1, 3]

        expected_filtered_list = ["banana", "date"]

        filter_string_list_by_index_list = FilterStringListByIndexList()
        result_filtered_list = filter_string_list_by_index_list.run(string_list, index_list)

        self.assertEqual(result_filtered_list, (expected_filtered_list,))

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

class TestRandomNormalDist(unittest.TestCase):
    def test_custom_num_samples(self):
        mean = 0.0
        std_dev = 1.0
        num_samples = 5
        min_value = 5.0
        max_value = 8.0

        rnd = RandomNormalDist()
        result = rnd.run(mean, std_dev, num_samples, min_value, max_value)

        self.assertEqual(len(result[0]), num_samples)

    @patch('random.gauss')
    def test_custom_min_max_values(self, mock_gauss):
        mock_gauss.side_effect = [4.0, 9.0, 6.0]

        mean = 0.0
        std_dev = 1.0
        num_samples = 3
        min_value = 5.0
        max_value = 8.0

        rnd = RandomNormalDist()
        result = rnd.run(mean, std_dev, num_samples, min_value, max_value)

        self.assertEqual(result[0], [5.0, 8.0, 6.0])
        self.assertEqual(result[1], 5.0)

    @patch('random.gauss')
    def test_values_within_range(self, mock_gauss):
        mock_gauss.side_effect = [4.5, 5.5, 7.5, 8.5]

        mean = 0.0
        std_dev = 1.0
        num_samples = 4
        min_value = 5.0
        max_value = 8.0

        rnd = RandomNormalDist()
        result = rnd.run(mean, std_dev, num_samples, min_value, max_value)

        self.assertEqual(result[0], [5.0, 5.5, 7.5, 8.0])
        self.assertEqual(result[1], 5.0)

if __name__ == '__main__':
    unittest.main()
