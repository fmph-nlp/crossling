#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function

from collections import Counter
from docopt import docopt
import sys


def main():
    args = docopt("""
    Usage:
        tsv2pairs.py [options] <corpus> <output>

    Example:
        tsv2pairs.py eubookshop.tsv pairs

    Options:
        --thr NUM    The minimal word count for being in the vocabulary [default: 2]
        --vocabs     Write vocabularies to <lang>.vocab files
    """)

    corpus_file = args['<corpus>']
    output = args['<output>']
    thr = int(args['--thr'])
    save_vocabs = args['--vocabs']

    print('Extracting vocabularies.')
    vocabs = read_vocabs(corpus_file, thr)

    if save_vocabs:
        print('Saving vocabs to files...')
        write_vocabs(vocabs)

    print('Reading pairs.')
    with open(output, 'wb') as outfile:
        read_pairs(corpus_file, vocabs, outfile)


def read_vocabs(corpus_filename, thr):
    vocabs = {}

    def update_vocab(lang, text):
        try:
            vocabs[lang].update(Counter(text.split(' ')))
        except KeyError:
            vocabs[lang] = Counter(text.split(' '))

    idx = 1
    with open(corpus_filename) as corpus:
        for line in corpus:
            lang, text = line.strip().split('\t')
            update_vocab(lang, text)

            if idx % 1000 == 0:
                print('line %s' % idx, end='\r')
                sys.stdout.flush()

    return dict([(lang, dict([(token, count) for token, count in vocabs[lang].items() if count >= thr])) for lang in vocabs.iterkeys()])


def read_pairs(corpus_filename, vocabs, outfile):
    idx = 1

    def extract_pairs(lang, text, sentence_id):
        for word in text.split(' '):
            if word in vocabs[lang]:
                print(''.join((lang, '_', word, ' ', str(sentence_id))), file=outfile)

    with open(corpus_filename) as corpus:
        for line in corpus:
            lang, text = line.strip().split('\t')

            if idx % 1000 == 0:
                print('line %s' % idx, end='\r')
                sys.stdout.flush()

            extract_pairs(lang, text, idx)
            idx += 1


def write_vocabs(vocabs):
    for lang, vocab in vocabs.iteritems():
        name = '%s.vocab' % lang
        print('    %s' % name)
        with open(name, 'wb') as outfile:
            for token, count in vocab.items():
                print('%s\t%d' % (token, count), file=outfile)


if __name__ == '__main__':
    main()

