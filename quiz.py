'''
Simple script to correctly calculate the 'correct' notes and chords in a key
'''


'''
Example:

What is the [3rd] of [C] [Maj]?

Expects the Answer: E (or E Maj)

'''

'''

Brainstorm

* Design function to calculate intervals
* Build relations such that intervals are calculated correctly
* Remember Major key scale intervals are 2.5 3.5 (C, D, E, F, G, A, B)
* For lists, major scale intervals are +2, +2, +1, +2, +2, +2, +1
* Natural Minor Key scale is 1.5, 2.5, 2 (A, B, C, D, E, F, G, A)
* For lists, natural minor scale intervals are +2, +1, +2, +2, +1, +2, +2
* Harmonic Minor Key scale is 1.5, 2.5, 1.5*, .5 *this is 1 stop (A, B, C, D, E, F, G#, A)
* For lists, harmonic minor scole intervals are +2, +1, +2, +2, +1, +3, +1
* All the notes C, C#, D, D#, E, F, F#, G, G#, A, A#, B
'''

CHROMA_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
MAJOR_HALF = [3, 7]
MINOR_HALF = [2, 5]
INTVAL = {'major': [3, 7], 'minor': [2, 5]}

def gen_key(note):
    '''
    Using the CHROMA_SCALE for reference, create the key.
    NOTE: This only works with major. May refactor.
    '''
    note = CHROMA_SCALE.index(note)
    key = []
    interval = 1
    while len(key) < 8:
        key.append(CHROMA_SCALE[note % len(CHROMA_SCALE)])
        if interval in INTVAL['major']:
            note += 1
        else:
            note += 2
        interval += 1
    return key


if __name__ == '__main__':
    g = gen_key('C')
    print g