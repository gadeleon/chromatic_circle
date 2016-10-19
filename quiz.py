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
* Remember Key scale intervals are 2.5 3.5 (C, D, E, F, G, A, B)
* For lists, scale intervals are +2, +2, +1, +2, +2, +2, +1
* All the notes C, C#, D, D#, E, F, F#, G, G#, A, A#, B
'''

CHROMA_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

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
        if interval == 3 or interval == 7:
            note += 1
        else:
            note += 2
        interval += 1
    return key


if __name__ == '__main__':
    g = gen_key('A')
    print g