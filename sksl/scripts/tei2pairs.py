#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function

import xml.etree.ElementTree as etree
from collections import Counter
from docopt import docopt
import sys
from nltk.tokenize import word_tokenize


def main():
    args = docopt("""
    Usage:
        tei2pairs.py [options] <corpus> <lang1> <lang2> <output>
        
    Example:
        tei2pairs.py jrc/alignedCorpus_sk_sl.xml sk sl

    Options:
        --thr NUM    The minimal word count for being in the vocabulary [default: 2]
        --vocabs     Write vocabularies to <lang>.vocab files
    """)

    corpus_file = args['<corpus>']
    lang1 = args['<lang1>']
    lang2 = args['<lang2>']
    output = args['<output>']
    thr = int(args['--thr'])
    save_vocabs = args['--vocabs']

    print('Extracting vocabularies.')
    vocabs = read_vocabs(corpus_file, thr, lang1, lang2)

    if save_vocabs:
        print('Saving vocabs to files...')
        write_vocabs(vocabs)

    print('Reading pairs.')
    with open(output, 'wb') as outfile:
        read_pairs(corpus_file, vocabs, lang1, lang2, outfile)


def read_vocabs(xml, thr, lang1, lang2):
    vocabs = {lang1: Counter(), lang2: Counter()}

    def update_vocab(lang, text):
        vocabs[lang].update(Counter(text.split(' ')))

    idx = 1
    for event, elem in etree.iterparse(xml, events=['start', 'end']):
        if event == 'start':
            if elem.tag == 'link':
                n_from, n_to = [int(x) for x in elem.attrib['type'].split('-')]
                if idx % 1000 == 0:
                    print('link %s' % idx, end='\r')
                    sys.stdout.flush()

        if event == 'end':
            if elem.tag == 's1':
                text = extract_sentence(elem, n_from)
                update_vocab(lang1, text)
                elem.clear()
            elif elem.tag == 's2':
                text = extract_sentence(elem, n_to)
                update_vocab(lang2, text)
                elem.clear()
            elif elem.tag == 'link':
                idx += 1
            elif elem.tag != 'p':
                elem.clear()

    return dict([(lang, dict([(token, count) for token, count in vocabs[lang].items() if count >= thr])) for lang in (lang1, lang2)])


def read_pairs(xml, vocabs, lang1, lang2, outfile):
    idx = 1

    def extract_pairs(lang, text, sentence_id):
        for word in text.split(' '):
            if word in vocabs[lang]:
                print(''.join((lang, '_', word.lower(), ' ', str(sentence_id))).encode("UTF-8"), file=outfile)

    for event, elem in etree.iterparse(xml, events=['start', 'end']):
        if event == 'start':
            if elem.tag == 'link':
                n_from, n_to = [int(x) for x in elem.attrib['type'].split('-')]
                if idx % 1000 == 0:
                    print('link %s' % idx, end='\r')
                    sys.stdout.flush()

        if event == 'end':
            if elem.tag == 's1':
                text = extract_sentence(elem, n_from)
                extract_pairs(lang1, text, idx)
                elem.clear()
            elif elem.tag == 's2':
                text = extract_sentence(elem, n_to)
                extract_pairs(lang2, text, idx)
                elem.clear()
            elif elem.tag == 'link':
                idx += 1
            elif elem.tag != 'p':
                elem.clear()


def extract_sentence(sent, n_pars):
    text = ''
    if n_pars == 1:
        text = sent.text
    elif n_pars > 1:
        pars = sent.findall('p')
        text = ' '.join([par.text for par in pars])
        for par in pars:
            par.clear()
    return ' '.join(word_tokenize(text))


def write_vocabs(vocabs):
    for lang, vocab in vocabs.iteritems():
        name = '%s.vocab' % lang
        print('    %s' % name)
        with open(name, 'wb') as outfile:
            for token, count in vocab.items():
                print('%s\t%d' % (token.encode("UTF-8"), count), file=outfile)


if __name__ == '__main__':
    main()

