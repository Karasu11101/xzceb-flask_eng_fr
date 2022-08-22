import unittest

def test_englishToFrench():
    englishText = 'Hello'
    self.assertTrue(englishText == 'Bonjour' )

def test_frenchToEnglish():
    frenchText = 'Bonjour'
    self.assertTrue(frenchText == 'Hello')


if __name__ == '__main__':
    unittest.main()
