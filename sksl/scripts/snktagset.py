#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

class Ufaltag:
    def __init__(self, s=None):
        self.pos = self.subpos = self.gender = self.number = self.case = self.possgender = '-'
        self.possnumber = self.person = self.tense = self.grade = self.negation = self.voice = '-'
        self.aspect = self.cond = self.var = self.vocal = self.aggl = '-'
        if s:
            self.pos, self.subpos, self.gender, self.number, self.case, self.possgender, \
            self.possnumber, self.person, self.tense, self.grade, self.negation, self.voice, \
            self.aspect, self.cond, self.var, self.vocal, self.aggl = s

    def __str__(self):
        return (self.pos + self.subpos + self.gender + self.number + self.case + self.possgender +
            self.possnumber + self.person + self.tense + self.grade + self.negation + self.voice +
            self.aspect + self.cond + self.var + self.vocal + self.aggl)


def snk2ufal(tag):
    "skonvertuje SNK tag do pozicneho systemu"
    "mierne sa snazi prisposobit prazskemu tagsetu"
    tag = tag.split(':')[0]
    res = Ufaltag()
    res.pos = tag[0]
    tag = tag[1:]
    if res.pos in 'SAPN':
        res.subpos = tag[0]
    for gender in 'mifnho':
        if gender in tag:
            res.gender = gender
    for number in 'sp':
        if number in tag:
            res.number = number
    for case in '1234567':
        if case in tag:
            res.case = case
    for person in 'abc':
        if person in tag:
            res.person = person
    for tense in 'IKMHLB':
        if tense in tag:
            res.tense = tense
    for grade in 'xyz':
        if grade in tag:
            res.grade = grade
    for negation in '+-':
        if negation in tag:
            res.negation = 'A' if negation=='+' else 'N'
    for voice in 'tk':
        if voice in tag:
            res.voice = voice
    for aspect in 'ejd':
        if aspect in tag:
            res.aspect = aspect
    if 'Y' in tag:
        res.cond = 'Y'
    if 'g' in tag:
        res.aggl = 'g'
    for vocal in 'uv':
        if vocal in tag:
            res.vocal = vocal

    return str(res)

def ufal2snk(tag):
    if len(tag) == 1: # symboly pre interpunkciu a cislice
        return tag
    tag = Ufaltag(tag)
    res = tag.pos
    if tag.pos == 'V':
        if tag.tense != '-':
            res += tag.tense
        if tag.aspect != '-':
            res += tag.aspect
        if tag.number != '-':
            res += tag.number
        if tag.person != '-':
            res += tag.person
        if tag.gender != '-':
            res += tag.gender
        if tag.negation == 'A':
            res += '+'
        elif tag.negation == 'N':
            res += '-'
        else:
            raise ValueError('Negation must be A or N')

    else:
        if tag.subpos != '-':
            res += tag.subpos
        if tag.voice != '-':
            res += tag.voice
        if tag.gender != '-':
            res += tag.gender
        if tag.number != '-':
            res += tag.number
        if tag.vocal != '-':
            res += tag.vocal
        if tag.case != '-':
            res += tag.case
        if tag.grade != '-':
            res += tag.grade
        if tag.cond != '-':
            res += tag.cond
        if tag.aggl != '-':
            assert tag.aggl == 'g'
            res += tag.aggl

    return res

def test():
    for line in sys.stdin:
        t = line.strip()
        ut =  snk2ufal(t)
        re_t = ufal2snk(ut)
        if re_t != t:
            print ut, t,  ufal2snk(ut)

def convertcolumn(coversion_function, column):
    for line in sys.stdin:
        if line.startswith('<'):
            if line.startswith('</s'):
                print
                continue
            else:
                continue
        elif not line.strip():
            print
            continue
        columns = line.strip().split('\t')
        row = []
        for i, c in enumerate(columns):
            if i==column:
                cell = coversion_function(c)
            else:
                cell = c
            row.append(cell)
        print '\t'.join(row)



if __name__ == '__main__':
    if sys.argv[1] == 'test':
        test()
    if sys.argv[1] == 'convertcolumn2ufal':
        column = int(sys.argv[2])
        convertcolumn(snk2ufal, column)
    elif sys.argv[1] == 'convertcolumn2snk':
        column = int(sys.argv[2])
        convertcolumn(ufal2snk, column)

