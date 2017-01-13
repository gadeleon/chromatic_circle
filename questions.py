'''
Questions generation functions
'''

import random


def degree(note, scale, degree):
    '''
    What is the <Number> of <Note> <Scale>?
    '''
    try:
        answer = raw_input('What is the {} of {} {}: '.format(str(degree + 1), note, scale.capitalize()))
        return answer, degree
    except KeyboardInterrupt:
        print '\nQUITTER!'
        raise SystemExit


def grade_degree(key, note, scale):
    deg = random.randint(0, 6)
    answer = key[deg]
    correct = False
    while not correct:
        my_answer, my_degree = degree(note, scale, deg)
        if my_answer == answer:
            print 'You Done got it Right!'
            correct = True
        else:
            continue


def triad(note, scale):
    '''
    What are the notes in a <NOTE> <Scale> triad?
    '''
    try:
        answer = raw_input('What notes are in a {} {} triad: '.format(note, scale.capitalize()))
        return answer
    except KeyboardInterrupt:
        print '\nQUITTER!'
        raise SystemExit


def grade_triad(key, note, scale):
    correct = False
    answer_triad = [key[0], key[2], key[4]]
    my_triad = []
    while not correct:
        answer = triad(note, scale)
        if ',' in answer:
            my_triad = answer.split(', ')
            print my_triad
            if len(my_triad) != 3:
                my_triad = answer.split(',')
        else:
            my_triad = answer.split(' ')
        if len(my_triad) != 3:
            print 'Answer with commas or spaces between notes'
            raise SystemExit
        validation = [i for i, x in zip(answer_triad, my_triad) if i == x]
        if len(validation) == 3:
            print 'You Done got it Right!  '
            correct = True
        else:
            continue
