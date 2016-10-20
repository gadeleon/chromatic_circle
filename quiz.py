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
* Remember Natural Major key scale intervals are 2.5 3.5 (C, D, E, F, G, A, B)
* For lists, major scale intervals are +2, +2, +1, +2, +2, +2, +1
* Natural Minor Key scale is 1.5, 2.5, 2 (A, B, C, D, E, F, G, A)
* For lists, natural minor scale intervals are +2, +1, +2, +2, +1, +2, +2
* All the notes C, C#, D, D#, E, F, F#, G, G#, A, A#, B
'''

CHROMA_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
MAJOR_HALF = [3, 7]
MINOR_HALF = [2, 5]
INTVAL = {'major': [3, 7], 'minor': [2, 5]}

def gen_key(note, scale):
    '''
    Using the CHROMA_SCALE for reference, create the key.
    NOTE: This only works with major. May refactor.
    '''
    note = CHROMA_SCALE.index(note)
    scale = scale.lower()
    key = []
    interval = 1
    while len(key) < 8:
        key.append(CHROMA_SCALE[note % len(CHROMA_SCALE)])
        try:
            if interval in INTVAL[scale]:
                note += 1
            else:
                note += 2
            interval += 1
        except KeyError:
            print 'Scale must be "major" or "minor"; {} entered'.format(scale)
            raise SystemExit
    return key


if __name__ == '__main__':
    g = gen_key('C', 'major')
    print g
    a = gen_key('A', 'minor')
    print a