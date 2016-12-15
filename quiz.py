'''
Script to correctly calculate the 'correct' notes and chords in a key
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
* Have quiz pull from valid pool of letters (ie )
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
Sharps and flats aren't allowed to mix/be in the same signature. So with that in mind, D# *has* to become Eb.
Because of these two rules, we change the signature one final time
['D#', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb] > ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb]

While D# and it's degrees are 100-percent valid as tones. D# cannot be written as a root. (Well, it can but not for CoF)
D# should become Eb in the program.

Will need to display the question as "What is the [3rd] of [Eb] [Major]" but the back end, it would look something like
print "What is the [Random Degree] of [KeySig[0]] [Major/Minor]"






'''

'''
Tone objects to make it easy to switch between flats, naturals, and sharps?
How?

B# = C = Dbb

B## = C# = Db

C## = D = Ebb

C### = D# = Eb

D## = E = Fb

E# = F = Gbb

E## = F# = Gb

F## = G = Abb

F### = G# = Ab

G## = A = Bbb

G### = A# = Bb

A## = B = Cb

Can that relation be calculated?

Calculate distance between notes. Having a positive number converts to flats, negatives to sharps.
'''

import questions
import music_theory

import random


def gen_question():
    note = random.choice(music_theory.CIRCLE)
    q = [questions.grade_degree, questions.grade_triad]
    s = ['major', 'major']
    # s = ['major', 'minor']
    scale = random.choice(s)
    key = music_theory.gen_key_sig(note, scale)
    random.choice(q)(key, note, scale)


def main():
    '''
    for i in CHROMA_SCALE:
        sig = gen_key_sig(i, 'major')
        print sig
    sharps = ['C', 'G', 'D', 'A', 'E', 'B', 'F#']
    flats = ['Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F']
    #sig = gen_key_sig('Ab', 'major')
    for i in sharps:
        sig = gen_key_sig(i, 'major')
        print sig
    for i in flats:
        sig = gen_key_sig(i, 'major')
        print sig
    sig = gen_key_sig('Ab', 'major')
    print sig
    '''
    gen_question()

if __name__ == '__main__':
    main()
