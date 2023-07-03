import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 

    def test1(self): 
        self.assertEqual(englishToFrench('hello'), 'bonjour') 
        self.assertEqual(englishToFrench("goodbye"), 'au revoir') 
    
 
class TestFrenchToEnglish(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(frenchToEnglish('bonjour'), 'hello')         
        self.assertEqual(frenchToEnglish('au revoir'), 'goodbye') 
        
unittest.main()