import os
from os import path
import sys
import math
from functools import partial

from docopt import docopt
import numpy as np
from scipy import spatial


def main():
    args = docopt("""
    Usage:
        nearest.py [options] <vecs1> <vecs2> <vocab1> <vocab2> <word> <lang> <num_results>

    Example:
        nearest.py sk.lemmas sl.lemmas model.pth
    """)

    vecs1_file = args['<vecs1>']
    vecs2_file = args['<vecs2>']
    vocab1_file = args['<vocab1>']
    vocab2_file = args['<vocab2>']
    word = args['<word>']
    lang = args['<lang>']
    num_results = int(args['<num_results>'])

    print('Loading data...')
    vecs1 = np.load(vecs1_file)
    vecs2 = np.load(vecs2_file)
    vocab1 = [line.rstrip() for line in open(vocab1_file)]
    vocab2 = [line.rstrip() for line in open(vocab2_file)]

    word_index1 = {v: k for k, v in enumerate(vocab1)}
    word_index2 = {v: k for k, v in enumerate(vocab2)}

    print('Data loaded')

    if lang == 'sl':
        wordvec = vecs2[word_index2[word]]
    else:
        wordvec = vecs1[word_index1[word]]

    print('Computing similarities [sk]...')
    find_closest(wordvec, vecs1, vocab1, num_results)

    print('Computing similarities [sl]...')
    find_closest(wordvec, vecs2, vocab2, num_results)


def find_closest(wordvec, vecs, vocab, num_results):
    difs = np.apply_along_axis(partial(cos_difference, wordvec), 1, vecs)
    idx = np.argsort(difs)
    for i in range(num_results):
        print('word %2d with similarity %.4f: %s' % (i + 1, 1 - difs[idx[i]], vocab[idx[i]]))


def cos_difference(x, y):
    return spatial.distance.cosine(x, y)


def read_corpus(corpus_file, num_words):
    lines = []
    with open(corpus_file) as corpus:
        for line in corpus:
            lines.append(line.strip())

    tokenizer = text.Tokenizer(num_words=num_words,
                              lower=False,
                              oov_token='<unk>')

    tokenizer.fit_on_texts(lines)
    return tokenizer.texts_to_sequences(lines), tokenizer


if __name__ == '__main__':
    main()

