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
    '''
    note = CHROMA_SCALE.index(note)
    start = [CHROMA_SCALE[note]]
    note += 2
    start.append(CHROMA_SCALE[note])
    note += 2
    start.append(CHROMA_SCALE[note])
    note += 1
    start.append(CHROMA_SCALE[note])
    note += 2
    start.append(CHROMA_SCALE[note])
    note += 2
    start.append(CHROMA_SCALE[note])
    note += 2
    start.append(CHROMA_SCALE[note])
    note += 1
    start.append(CHROMA_SCALE[note % len(CHROMA_SCALE)])
    return start


if __name__ == '__main__':
    g = gen_key('C')
    print g