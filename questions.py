'''
Questions generation functions
'''


def degree(note, scale, degree):
    '''
    What is the <Number> of <Note> <Scale>?
    '''
    answer = raw_input('What is the {} of {} {}: '.format(str(degree + 1), note, scale.capitalize()))
    return answer, degree


def triad(note, scale):
    '''
    What are the notes in a <NOTE> <Scale> triad?
    '''
    answer = raw_input('What notes are in a {} {} triad: '.format(note, scale.capitalize()))
    return answer, note
