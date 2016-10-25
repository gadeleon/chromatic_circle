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

PITCH_SCALE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


class Tone(object):
    def __init__(self, note):
        self.note = note
        self.pitch = CHROMA_SCALE.index(note)
        self.note_flat = get_enharmonic(len(CHROMA_SCALE), self.note)
        self.note_sharp = get_enharmonic(len(CHROMA_SCALE), self.note, up=False)

    def __repr__(self):
        print self.note


def cheat_harmonic(note):
    root = CHROMA_SCALE.index(note)
    pos = LETTER_ORDER.index(note)
    key = []
    key.append(note)
    step = 1
    interval = 1
    while len(key) > 8:
        # Get next letter
        tone = LETTER_ORDER[(pos + step) % len(LETTER_ORDER)]
        # Get the next degree
        if interval in INTVAL['major']:
            root += 1
        else:
            root += 2
        interval += 1
        degree = CHROMA_SCALE[root % len(CHROMA_SCALE)]
        # Now get distance between tone[0]/next letter and the degree in chroma scale




def get_enharmonic(length, note, up=True):
    '''
    Gets the distance between two letter changes in order to express sharps and flats otherwise known as the
    enharmonic equivalent
    '''
    try:
        pos = CHROMA_SCALE.index(note)
    except ValueError:
        pos = CHROMA_SCALE.index(calc_pitch(note))
    steps = 0
    while CHROMA_SCALE[pos % length][0] == note[0]:
        if up:
            pos += 1
        else:
            pos -= 1
        steps += 1
    if up:
        flats = 'b' * steps
    else:
        flats = '#' * steps
    return '{}{}'.format(CHROMA_SCALE[pos % length], flats)



CHROMA_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
LETTER_ORDER = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
MAJOR_HALF = [3, 7]
MINOR_HALF = [2, 5]
INTVAL = {'major': [3, 7], 'minor': [2, 5]}

# Make a note of this pitch with this letter.

def get_pitch(note):
    note = note.upper()
    try:
        pitch = CHROMA_SCALE.index(note)
    except ValueError:
        pitch = CHROMA_SCALE.index(calc_pitch(note))
    return PITCH_SCALE[pitch]

def make_accidental(note, spelling):
    note = note.upper()
    spelling = spelling.upper()
    # Get Pos of pitch on CHROMA
    pitch = get_pitch(note)
    pos = CHROMA_SCALE[pitch]
    # Get the pos of the spelling we want
    spell_pitch = get_pitch(spelling)
    dist = pitch - spell_pitch
    if dist > 0:
        acd = '#' * dist
    else:
        acd = 'b' * abs(dist)
    return '{}{}'.format(spelling, acd)


def calc_pitch(note):
    '''
    Taken an accidental and gets the 'normal' note in the CHROMA SCALE
    '''
    root = CHROMA_SCALE.index(note[0])
    ac = note[1:]
    for i in ac:
        if i == '#':
            root += 1
        elif i == 'b':
            root -=1
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
    scale = scale.lower()
    key = []
    interval = 1
    while len(key) < 8:
        tone = CHROMA_SCALE[pos % len(CHROMA_SCALE)]
        ## FIXME: Make Sure next tone is the next letter
        if tone[0] not in key:
            key.append(tone)
        else:
            # What is next letter?
            #enh = LETTER_ORDER.index((note + 1) % len(LETTER_ORDER)
            if len(key) > 6:
                key.append(key[0])
                continue
            enharmonic = LETTER_ORDER[(LETTER_ORDER.index(note[0]) + 1) % len(LETTER_ORDER)][0]
            enh_pos = CHROMA_SCALE.index(enharmonic)
            dist = abs(pos - enh_pos)
            enharmonic = '{}{}'.format(enharmonic, '#' * dist)
            key.append(enharmonic)
        try:
            if interval in INTVAL[scale]:
                pos += 1
            else:
                pos += 2
            interval += 1
        except KeyError:
            print 'Scale must be "major" or "minor"; {} entered'.format(scale)
            raise SystemExit
    return key

def adjust_key(keysig):
    '''
    Looks at key generated from gen_key_sig and corrects for flats and sharps
    '''
    for i in range(len(keysig)):
        try:
            if keysig[i % len(keysig)][0] == keysig[(i+1) % len(keysig)][0] and (keysig[(i-1) % len(keysig)][-1] == keysig[(i+1) % len(keysig)][-1]):
                if i != 7:
                    keysig[(i) % len(keysig)] = get_enharmonic(len(CHROMA_SCALE), keysig[(i) % len(keysig)], up=False)
            elif keysig[i % len(keysig)][0] == keysig[(i+1) % len(keysig)][0]:
                keysig[(i+1) % len(keysig)] = get_enharmonic(len(CHROMA_SCALE), keysig[(i+1) % len(keysig)])
            else:
                pass
        except IndexError:
            raise
    if keysig[-1] != keysig[0]:
        keysig[0] = keysig[-1]
    # Do it one more time!
    return keysig


if __name__ == '__main__':
    # ds = gen_key_sig('D#', 'major')
    # print ds    
    # ds = adjust_key(ds) 
    # print ds
    #a = gen_key_sig('C', 'minor')
    #print a
    for i in CHROMA_SCALE:
        sig = gen_key_sig(i, 'major')
        print sig
        sig = adjust_key(sig)
        print sig