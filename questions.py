'''
Questions generation functions
'''

import quiz
import random


def degree(note, scale):
    '''
    What is the <Number> of <Note> <Scale>?
    '''
    deg = random.randint(0, 6)
    answer = raw_input('What is the {} of {} {}: '.format(str(deg + 1), note, scale))
    return answer, deg
