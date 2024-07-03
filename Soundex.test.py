# import unittest
# from Soundex import generate_soundex

# class TestSoundex(unittest.TestCase):

#     def test_empty_string(self):
#         self.assertEqual(generate_soundex(""), "")

#     def test_single_character(self):
#         self.assertEqual(generate_soundex("A"), "A000")

    
# if __name__ == '__main__':
#     unittest.main()
import unittest

class SoundexTests(unittest.TestCase):

    def test_get_soundex_code(self):
        self.assertEqual(get_soundex_code('B'), '1')
        self.assertEqual(get_soundex_code('Z'), '2')
        self.assertEqual(get_soundex_code('T'), '3')
        self.assertEqual(get_soundex_code('L'), '4')
        self.assertEqual(get_soundex_code('N'), '5')
        self.assertEqual(get_soundex_code('R'), '6')
        self.assertEqual(get_soundex_code('X'), '2')  # Test a non-primary letter
        self.assertEqual(get_soundex_code('1'), '0')  # Test a non-alphabetic character
        self.assertEqual(get_soundex_code('*'), '0')  # Test another non-alphabetic character

    def test_generate_soundex(self):
        self.assertEqual(generate_soundex('Smith'), 'S530')
        self.assertEqual(generate_soundex('Johnson'), 'J525')
        self.assertEqual(generate_soundex('Williams'), 'W452')
        self.assertEqual(generate_soundex('Lee'), 'L000')  # Test short name
        self.assertEqual(generate_soundex('Nguyen'), 'N500')  # Test name with non-primary letter

    def test_generate_soundex_empty(self):
        self.assertEqual(generate_soundex(''), '')

    def test_generate_soundex_non_alpha(self):
        self.assertEqual(generate_soundex('123'), '0000')  # Test numeric input
        self.assertEqual(generate_soundex('*&^%'), '0000')  # Test special characters

if __name__ == '__main__':
    unittest.main()
