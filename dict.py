from string import ascii_uppercase
from copy import deepcopy
import actr

l = [['A-first', 'isa', 'outline', 'letter', "'a'", 'count', 'first', 'start-coor', 'c01', 'dest-coor', 'c10'],
['A-second', 'isa', 'outline', 'letter', "'a'", 'count', 'second', 'start-coor', 'c10', 'dest-coor', 'c20'],
['A-third', 'isa', 'outline', 'letter', "'a'", 'count', 'third', 'start-coor', 'c01', 'dest-coor', 'c12'],
['A-fourth', 'isa', 'outline', 'letter', "'a'", 'count', 'fourth', 'start-coor', 'c12', 'dest-coor', 'c22'],
['A-fifth', 'isa', 'outline', 'letter', "'a'", 'count', 'fifth', 'start-coor', 'c10', 'dest-coor', 'c12'],
['B-first', 'isa', 'outline', 'letter', "'b'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c02'],
['B-second', 'isa', 'outline', 'letter', "'b'", 'count', 'second', 'start-coor', 'c02', 'dest-coor', 'c12'],
['B-third', 'isa', 'outline', 'letter', "'b'", 'count', 'third', 'start-coor', 'c12', 'dest-coor', 'c10'],
['B-fourth', 'isa', 'outline', 'letter', "'b'", 'count', 'fourth', 'start-coor', 'c12', 'dest-coor', 'c22'],
['B-fifth', 'isa', 'outline', 'letter', "'b'", 'count', 'fifth', 'start-coor', 'c22', 'dest-coor', 'c20'],
['B-sixth', 'isa', 'outline', 'letter', "'b'", 'count', 'sixth', 'start-coor', 'c00', 'dest-coor', 'c20'],
['C-first', 'isa', 'outline', 'letter', "'c'", 'count', 'first', 'start-coor', 'c02', 'dest-coor', 'c00'],
['C-second', 'isa', 'outline', 'letter', "'c'", 'count', 'second', 'start-coor', 'c00', 'dest-coor', 'c20'],
['C-third', 'isa', 'outline', 'letter', "'c'", 'count', 'third', 'start-coor', 'c20', 'dest-coor', 'c22'],
['D-first', 'isa', 'outline', 'letter', "'d'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['D-second', 'isa', 'outline', 'letter', "'d'", 'count', 'second', 'start-coor', 'c00', 'dest-coor', 'c01'],
['D-third', 'isa', 'outline', 'letter', "'d'", 'count', 'third', 'start-coor', 'c01', 'dest-coor', 'c12'],
['D-fourth', 'isa', 'outline', 'letter', "'d'", 'count', 'fourth', 'start-coor', 'c12', 'dest-coor', 'c21'],
['D-fifth', 'isa', 'outline', 'letter', "'d'", 'count', 'fifth', 'start-coor', 'c21', 'dest-coor', 'c20'],
['E-first', 'isa', 'outline', 'letter', "'e'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['E-second', 'isa', 'outline', 'letter', "'e'", 'count', 'second', 'start-coor', 'c00', 'dest-coor', 'c02'],
['E-third', 'isa', 'outline', 'letter', "'e'", 'count', 'third', 'start-coor', 'c10', 'dest-coor', 'c12'],
['E-fourth', 'isa', 'outline', 'letter', "'e'", 'count', 'fourth', 'start-coor', 'c20', 'dest-coor', 'c22'],
['F-first', 'isa', 'outline', 'letter', "'f'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['F-second', 'isa', 'outline', 'letter', "'f'", 'count', 'second', 'start-coor', 'c00', 'dest-coor', 'c02'],
['F-third', 'isa', 'outline', 'letter', "'f'", 'count', 'third', 'start-coor', 'c10', 'dest-coor', 'c12'],
['G-first', 'isa', 'outline', 'letter', "'g'", 'count', 'first', 'start-coor', 'c02', 'dest-coor', 'c00'],
['G-second', 'isa', 'outline', 'letter', "'g'", 'count', 'second', 'start-coor', 'c00', 'dest-coor', 'c20'],
['G-third', 'isa', 'outline', 'letter', "'g'", 'count', 'third', 'start-coor', 'c20', 'dest-coor', 'c22'],
['G-fourth', 'isa', 'outline', 'letter', "'g'", 'count', 'fourth', 'start-coor', 'c22', 'dest-coor', 'c12'],
['G-fifth', 'isa', 'outline', 'letter', "'g'", 'count', 'fifth', 'start-coor', 'c12', 'dest-coor', 'c11'],
['H-first', 'isa', 'outline', 'letter', "'h'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['H-second', 'isa', 'outline', 'letter', "'h'", 'count', 'second', 'start-coor', 'c10', 'dest-coor', 'c12'],
['H-third', 'isa', 'outline', 'letter', "'h'", 'count', 'third', 'start-coor', 'c02', 'dest-coor', 'c22'],
['I-first', 'isa', 'outline', 'letter', "'i'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c02'],
['I-second', 'isa', 'outline', 'letter', "'i'", 'count', 'second', 'start-coor', 'c01', 'dest-coor', 'c21'],
['I-third', 'isa', 'outline', 'letter', "'i'", 'count', 'third', 'start-coor', 'c20', 'dest-coor', 'c22'],
['J-first', 'isa', 'outline', 'letter', "'j'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c02'],
['J-second', 'isa', 'outline', 'letter', "'j'", 'count', 'second', 'start-coor', 'c01', 'dest-coor', 'c21'],
['J-third', 'isa', 'outline', 'letter', "'j'", 'count', 'third', 'start-coor', 'c21', 'dest-coor', 'c20'],
['K-first', 'isa', 'outline', 'letter', "'k'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['K-second', 'isa', 'outline', 'letter', "'k'", 'count', 'second', 'start-coor', 'c02', 'dest-coor', 'c10'],
['K-third', 'isa', 'outline', 'letter', "'k'", 'count', 'third', 'start-coor', 'c10', 'dest-coor', 'c22'],
['L-first', 'isa', 'outline', 'letter', "'l'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['L-second', 'isa', 'outline', 'letter', "'l'", 'count', 'second', 'start-coor', 'c20', 'dest-coor', 'c22'],
['M-first', 'isa', 'outline', 'letter', "'m'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['M-second', 'isa', 'outline', 'letter', "'m'", 'count', 'second', 'start-coor', 'c00', 'dest-coor', 'c21'],
['M-third', 'isa', 'outline', 'letter', "'m'", 'count', 'third', 'start-coor', 'c21', 'dest-coor', 'c02'],
['M-fourth', 'isa', 'outline', 'letter', "'m'", 'count', 'fourth', 'start-coor', 'c02', 'dest-coor', 'c22'],
['N-first', 'isa', 'outline', 'letter', "'n'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['N-second', 'isa', 'outline', 'letter', "'n'", 'count', 'second', 'start-coor', 'c00', 'dest-coor', 'c22'],
['N-third', 'isa', 'outline', 'letter', "'n'", 'count', 'third', 'start-coor', 'c02', 'dest-coor', 'c22'],
['O-first', 'isa', 'outline', 'letter', "'o'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['O-second', 'isa', 'outline', 'letter', "'o'", 'count', 'second', 'start-coor', 'c20', 'dest-coor', 'c22'],
['O-third', 'isa', 'outline', 'letter', "'o'", 'count', 'third', 'start-coor', 'c22', 'dest-coor', 'c02'],
['O-fourth', 'isa', 'outline', 'letter', "'o'", 'count', 'fourth', 'start-coor', 'c02', 'dest-coor', 'c00'],
['P-first', 'isa', 'outline', 'letter', "'p'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['P-second', 'isa', 'outline', 'letter', "'p'", 'count', 'second', 'start-coor', 'c00', 'dest-coor', 'c02'],
['P-third', 'isa', 'outline', 'letter', "'p'", 'count', 'third', 'start-coor', 'c02', 'dest-coor', 'c12'],
['P-fourth', 'isa', 'outline', 'letter', "'p'", 'count', 'fourth', 'start-coor', 'c12', 'dest-coor', 'c10'],
['Q-first', 'isa', 'outline', 'letter', "'q'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['Q-second', 'isa', 'outline', 'letter', "'q'", 'count', 'second', 'start-coor', 'c20', 'dest-coor', 'c21'],
['Q-third', 'isa', 'outline', 'letter', "'q'", 'count', 'third', 'start-coor', 'c21', 'dest-coor', 'c12'],
['Q-fourth', 'isa', 'outline', 'letter', "'q'", 'count', 'fourth', 'start-coor', 'c12', 'dest-coor', 'c02'],
['Q-fifth', 'isa', 'outline', 'letter', "'q'", 'count', 'fifth', 'start-coor', 'c02', 'dest-coor', 'c00'],
['Q-sixth', 'isa', 'outline', 'letter', "'q'", 'count', 'sixth', 'start-coor', 'c11', 'dest-coor', 'c22'],
['R-first', 'isa', 'outline', 'letter', "'r'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['R-second', 'isa', 'outline', 'letter', "'r'", 'count', 'second', 'start-coor', 'c00', 'dest-coor', 'c02'],
['R-third', 'isa', 'outline', 'letter', "'r'", 'count', 'third', 'start-coor', 'c02', 'dest-coor', 'c12'],
['R-fourth', 'isa', 'outline', 'letter', "'r'", 'count', 'fourth', 'start-coor', 'c12', 'dest-coor', 'c10'],
['R-fifth', 'isa', 'outline', 'letter', "'r'", 'count', 'fifth', 'start-coor', 'c10', 'dest-coor', 'c22'],
['S-first', 'isa', 'outline', 'letter', "'s'", 'count', 'first', 'start-coor', 'c02', 'dest-coor', 'c00'],
['S-second', 'isa', 'outline', 'letter', "'s'", 'count', 'second', 'start-coor', 'c00', 'dest-coor', 'c10'],
['S-third', 'isa', 'outline', 'letter', "'s'", 'count', 'third', 'start-coor', 'c10', 'dest-coor', 'c12'],
['S-fourth', 'isa', 'outline', 'letter', "'s'", 'count', 'fourth', 'start-coor', 'c12', 'dest-coor', 'c22'],
['S-fifth', 'isa', 'outline', 'letter', "'s'", 'count', 'fifth', 'start-coor', 'c22', 'dest-coor', 'c20'],
['T-first', 'isa', 'outline', 'letter', "'t'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c02'],
['T-second', 'isa', 'outline', 'letter', "'t'", 'count', 'second', 'start-coor', 'c01', 'dest-coor', 'c21'],
['U-first', 'isa', 'outline', 'letter', "'u'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['U-second', 'isa', 'outline', 'letter', "'u'", 'count', 'second', 'start-coor', 'c20', 'dest-coor', 'c22'],
['U-third', 'isa', 'outline', 'letter', "'u'", 'count', 'third', 'start-coor', 'c22', 'dest-coor', 'c02'],
['V-first', 'isa', 'outline', 'letter', "'v'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c10'],
['V-second', 'isa', 'outline', 'letter', "'v'", 'count', 'second', 'start-coor', 'c10', 'dest-coor', 'c21'],
['V-third', 'isa', 'outline', 'letter', "'v'", 'count', 'third', 'start-coor', 'c21', 'dest-coor', 'c12'],
['V-fourth', 'isa', 'outline', 'letter', "'v'", 'count', 'fourth', 'start-coor', 'c12', 'dest-coor', 'c02'],
['W-first', 'isa', 'outline', 'letter', "'w'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c20'],
['W-second', 'isa', 'outline', 'letter', "'w'", 'count', 'second', 'start-coor', 'c20', 'dest-coor', 'c11'],
['W-third', 'isa', 'outline', 'letter', "'w'", 'count', 'third', 'start-coor', 'c11', 'dest-coor', 'c22'],
['W-fourth', 'isa', 'outline', 'letter', "'w'", 'count', 'fourth', 'start-coor', 'c22', 'dest-coor', 'c02'],
['X-first', 'isa', 'outline', 'letter', "'x'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c22'],
['X-second', 'isa', 'outline', 'letter', "'x'", 'count', 'second', 'start-coor', 'c20', 'dest-coor', 'c02'],
['Y-first', 'isa', 'outline', 'letter', "'y'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c11'],
['Y-second', 'isa', 'outline', 'letter', "'y'", 'count', 'second', 'start-coor', 'c02', 'dest-coor', 'c11'],
['Y-third', 'isa', 'outline', 'letter', "'y'", 'count', 'third', 'start-coor', 'c11', 'dest-coor', 'c21'],
['Z-first', 'isa', 'outline', 'letter', "'z'", 'count', 'first', 'start-coor', 'c00', 'dest-coor', 'c02'],
['Z-second', 'isa', 'outline', 'letter', "'z'", 'count', 'second', 'start-coor', 'c02', 'dest-coor', 'c20'],
['Z-third', 'isa', 'outline', 'letter', "'z'", 'count', 'third', 'start-coor', 'c20', 'dest-coor', 'c22']]


def make_chunk_defs():
    m = deepcopy(l)

    alphabet = list(ascii_uppercase)

    chunk_defs = dict()
    for letter in alphabet:
        chunk_defs[letter] = []
        cell = chunk_defs[letter]
        while (len(m) > 0 and m[0][0][0] == letter):
            cell.append(m.pop(0))

    return chunk_defs

def make_chunk_names(chunk_defs):

    chunk_names = dict()
    for letter in chunk_defs:
        chunk_names[letter] = []
        cell = chunk_names[letter]
        for chunk in chunk_defs[letter]:
            cell.append(actr.define_chunks(chunk))

    return chunk_names
