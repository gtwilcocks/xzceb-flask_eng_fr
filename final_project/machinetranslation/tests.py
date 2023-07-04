"""This module tests the translator module.
"""

import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """Tests the english_to_french function in the translator module.
    """
    def test1(self):
        """Tests the english_to_french function in the translator module.
        """
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertEqual(english_to_french("goodbye"), 'au revoir')

class TestFrenchToEnglish(unittest.TestCase):
    """Tests the french_to_english function in the translator module.
    """
    def test2(self):
        """Tests the french_to_english function in the translator module.
        """
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertEqual(french_to_english('au revoir'), 'goodbye')

unittest.main()
