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

import random

PITCH_SCALE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
CHROMA_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
LETTER_ORDER = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
MAJOR_HALF = [3, 7]
MINOR_HALF = [2, 5]
INTVAL = {'major': [3, 7], 'minor': [2, 5]}
CIRCLE = ['C', 'G', 'D', 'A', 'E', 'B', 'Gb', 'F#', 'Db', 'C#', 'Ab', 'Eb', 'Bb', 'F']


def get_pitch(note):
    '''
    Gets the number in PITCH_SCALE which is 1:1 with CHROMA_SCALE
    but can be used to get accidentals.
    '''
    note = note.upper()
    try:
        pitch = CHROMA_SCALE.index(note)
    except ValueError:
        pitch = CHROMA_SCALE.index(calc_pitch(note))
    return PITCH_SCALE[pitch]


def make_accidental(note, spelling):
    note = note.upper()
    spelling = spelling.upper()
    # print 'Making {} in the context of {}'.format(note, spelling)
    # Get index of pitch on CHROMA
    pitch = get_pitch(note)
    # Get the index of the spelling we want
    spell_pitch = get_pitch(spelling)
    dist = pitch - spell_pitch
    if dist > 0:
        acd = '#' * dist
        if len(acd) > 3:
            acd = 'b' * (dist % 10)
    else:
        acd = 'b' * abs(dist)
        if len(acd) > 3:
            acd = '#' * abs(dist % 12)
    return '{}{}'.format(spelling, acd)


def calc_pitch(note):
    '''
    Taken an accidental and gets the 'normal' note in the CHROMA SCALE
    '''
    note = note.upper()
    root = CHROMA_SCALE.index(note[0])
    ac = note[1:]
    for i in ac:
        if i == '#':
            root += 1
        elif i == 'b'.upper():
            root -= 1
    return CHROMA_SCALE[root % len(CHROMA_SCALE)]


def gen_key_sig(note, scale):
    '''
    Using the CHROMA_SCALE for reference, create the key.
    NOTE: This only works with major. May refactor.
    '''
    try:
        pos = CHROMA_SCALE.index(note)
    except ValueError:
        pos = CHROMA_SCALE.index(calc_pitch(note))
    spelling = LETTER_ORDER.index(note[0])
    scale = scale.lower()
    key = []
    interval = 1
    while len(key) < 8:
        context = LETTER_ORDER[spelling % len(LETTER_ORDER)]
        if len(key) == 0:
            enharmonic = make_accidental(CHROMA_SCALE[pos % len(CHROMA_SCALE)], context)
            key.append(enharmonic)
        elif 0 < len(key) < 7:
            context = LETTER_ORDER[spelling % len(LETTER_ORDER)]
            enharmonic = make_accidental(CHROMA_SCALE[pos % len(CHROMA_SCALE)], context)
            key.append(enharmonic)
        elif len(key) > 6:
            key.append(key[0])
            continue
        try:
            if interval in INTVAL[scale]:
                pos += 1
            else:
                pos += 2
            interval += 1
            spelling += 1
        except KeyError:
            print 'Scale must be "major" or "minor"; {} entered'.format(scale)
            raise SystemExit
    return key


def grade_degree(key, note, scale):
    deg = random.randint(0, 6)
    correct = False
    while not correct:
        answer, degree = questions.degree(note, scale, deg)
        if key[(degree) % len(key)] == answer:
            print 'You Done got it Right!'
            correct = True
        else:
            continue


def grade_triad(key, note, scale):
    correct = False
    while not correct:
        answer, note = questions.triad(note, scale)
        answer_triad = [key[0], key[2], key[4]]
        #print answer_triad
        my_triad = []
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
        #print validation
        if len(validation) == 3:
            print 'You Done got it Right!  '
            correct = True
        else:
            continue


def gen_question():
    #scale = random.randint(0,1)
    note = CIRCLE[random.randint(0, (len(CIRCLE)-1))]
    q = [grade_degree, grade_triad]
    s = ['major', 'major']
    # s = ['major', 'minor']
    scale = random.choice(s)
    key = gen_key_sig(note, scale)
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
