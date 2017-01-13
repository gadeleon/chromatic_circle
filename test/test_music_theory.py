'''
Unit tests for music_theory.py
'''

import unittest

import music_theory


class RunKeyTestCase(unittest.TestCase):

    '''Tests for music_theory module'''

    def setUp(self):
        '''
        Called before testing
        '''
        pass

    def test_lowercase_valid(self):
        '''
        Assert 3rd of lowercase, valid letter, is the correct 3rd.
        '''
        self.assertEqual('D#', music_theory.gen_key_sig('b', 'major')[2])

    def test_invalid_letter_note(self):
        '''
        Feed a letter that is not a note.
        '''
        with self.assertRaises(ValueError) as context:
            music_theory.gen_key_sig('H', 'major')

    def test_incorrect_third(self):
        '''
        Assert the Third of C is F (it's actually E)
        '''
        self.assertNotEqual('F', music_theory.gen_key_sig('C', 'major')[2])


if __name__ == '__main__':
    unittest.main()
