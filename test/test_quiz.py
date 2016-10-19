'''
Unit tests for quiz.py
'''

import unittest

import quiz

class RunKeyTestCase(unittest.TestCase):

    '''Tests for run_report'''

    def setUp(self):
        '''
        Called before testing
        '''
        pass

    def test_incorrect_third(self):
        '''
        Assert the Third of C is F (it's actually E)
        '''
        self.assertEqual('F', quiz.gen_key('C')[2])
        


if __name__ == '__main__':
    unittest.main()
