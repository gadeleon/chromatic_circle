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
* Remember Key scale is 2.5 3.5 (C, D, E, F, G, A, B)
* All the notes C, C#, D, D#, E, F, F#, G, G#, A, A#, B
'''

CHROMA_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#']

def gen_key(note):
    '''
    Using the CHROMA_SCALE for reference, create the key.
    '''
    start = [CHROMA_SCALE[CHROMA_SCALE.index(note)]]
    return start


if __name__ == '__main__':
    gen_key('G')