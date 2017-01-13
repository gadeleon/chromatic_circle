'''
Music theory logic in python
'''

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
    '''
    "Spell" the variable note in the context of the variable spelling
    '''
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
    '''
    try:
        pos = CHROMA_SCALE.index(note)
    except ValueError:
        pos = CHROMA_SCALE.index(calc_pitch(note))
    # Make sure we grab only grab the letter from accidentals (eg, C from C#)
    try:
        spelling = LETTER_ORDER.index(note[0])
    except ValueError:
        note = note.upper()
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
        # Determine half step or whole step for next note
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
