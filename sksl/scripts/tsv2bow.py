#!/usr/bin/env python3

from collections import Counter
from docopt import docopt
import sys


def main():
    args = docopt("""
    Usage:
        tsv2bow.py [options] <corpus> <vocab> <output>

    Example:
        tsv2pairs.py eubookshop.tsv vocab eubookshop.bow
    """)

    corpus_file = args['<corpus>']
    vocab_file = args['<vocab>']
    output = args['<output>']

    print('Reading vocabulary...')
    with open(vocab_file) as vocab:
        vocab = read_vocab(vocab)

    print('Converting into BOW...')
    with open(corpus_file) as corpus:
        with open(output, 'w') as outfile:
            build_bow(corpus, vocab, outfile)


def read_vocab(vocab_file):
    vocab = {}
    idx = 1
    for line in vocab_file:
        token = line.strip().split('\t')[0]
        vocab[token] = idx
        idx += 1
    return vocab


def build_bow(corpus, vocab, outfile):
    idx = 0
    notfound = 0

    for line in corpus:
        if idx % 1000 == 0:
            print('line %s' % idx, end='\r')
            sys.stdout.flush()

        try:
            text = line.strip().split('\t')[1]
        except IndexError:
            text = ''
        tokens = text.strip().split(' ')
        indices = []
        for token in tokens:
            try:
                indices.append(str(vocab[token]))
            except KeyError as e:
                notfound += 1

        outfile.write(' '.join(indices) + '\n')

        idx += 1
    print('%d tokens not found in vocabulary (possibly due to thresholding) skipped' % notfound, file=sys.stderr)


if __name__ == '__main__':
    main()

