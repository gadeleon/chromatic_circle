'''
Simple script to correctly calculate the 'correct' notes and chords in a key
'''


'''
Example:

What is the [3rd] of [C] [Maj]?

Expects the Answer: E (or E Maj)

What notes are in a [C] [major chord] (triad?)?

Expects the Answer: C E G

'''

'''

Brainstorm

* Design function to calculate intervals
* Build relations such that intervals are calculated correctly
* Remember Natural Major key scale intervals are 2.5 3.5 (C, D, E, F, G, A, B)
* For lists, major scale intervals are +2, +2, +1, +2, +2, +2, +1
* Natural Minor Key scale is 1.5, 2.5, 2 (A, B, C, D, E, F, G, A)
* For lists, natural minor scale intervals are +2, +1, +2, +2, +1, +2, +2
* In writing the notes of a scale, it is customary that each scale degree be assigned with a successive letter.
* All the notes C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B
'''

'''
Correcting Signatures for Flats & Sharps

1. Ensure there's A - G in the signature. Adjust accordingly.
2. If notes had to flip to flat, switch the tonic.
3. Adjust existing signature is back to A - G.

Example:

D# (Normally Eb)
D#'s Key Signature is ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D', 'D#']

First, Correct the letters. G appears twice, so we correct the second G to Ab.
['D#', 'F', 'G', 'G#', 'A#', 'C', 'D', 'D#'] > ['D#', 'F', 'G', 'Ab', 'A#', 'C', 'D', 'D#']

Now A is being repeated. So we change the second A to Bb
['D#', 'F', 'G', 'Ab', 'A#', 'C', 'D', 'D#'] > ['D#', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'D#']

D repeats itself though. Let's make the 8th (the octave) Eb to keep proper syntax.
['D#', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'D#'] > ['D#', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb]

Since we changed the octave, we should have the tonic match for consistency.
['D#', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb] > ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb]

Therefore, 'D#' is not actually a valid key and would rename itself to Eb in the program


Sharps and flats aren't allowed to mix/be in the same signature. So with that in mind, D# *has* to become Eb.




'''

'''
Tone objects to make it easy to switch between flats, naturals, and sharps?
How?

B# = C = Db

Can that relation be calculated?
'''

class Tone(object):
    def __init__(self):
        self.natural = natural,
        self.flat = flat
        self.sharp = sharp

class KeySig(object):
    def __init__(self, key):
        self.key = key

CHROMA_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
MAJOR_HALF = [3, 7]
MINOR_HALF = [2, 5]
INTVAL = {'major': [3, 7], 'minor': [2, 5]}

def gen_key_sig(note, scale):
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
    g = gen_key_sig('C', 'major')
    print g
    for i in CHROMA_SCALE:
        s = gen_key_sig(i, 'major')
        print s
    a = gen_key_sig('A', 'minor')
    print a