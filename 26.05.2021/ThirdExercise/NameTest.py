from Name import Name
import unittest
from unittest.mock import patch


class TestValidInputs(unittest.TestCase):

    @patch('Name.Name.count_characters', return_value={'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    def test_count_characters(self, count_characters):
        self.assertEqual(Name.count_characters("Hello world"), {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

    @patch('Name.Name.count_words', return_value={'Hello': 1, 'world': 1})
    def test_count_words(self, count_words):
        self.assertEqual(Name.count_words("Hello world"), {'Hello': 1, 'world': 1})


if __name__ == "main":
    unittest.main()
