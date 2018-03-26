#!/usr/bin/python2

from os import listdir
from os.path import join
from collections import Counter
import sys


def main():
    thr = int(sys.argv[1])
    dir_path = sys.argv[2]
    for path in [join(dir_path, f) for f in listdir(dir_path) if f.endswith('.txt')]:
        language_prefix = path[-7:-4]
        with open(path) as fin:
            lines = [line.strip() for line in fin]
        vocab = read_vocab(lines, thr)
        extract_pairs(vocab, lines, language_prefix)


def extract_pairs(vocab, lines, language_prefix):
    for line in lines:
        sentence_id, sentence_str = line.split('\t')
        for word in sentence_str.split(' '):
            if word in vocab:
                print ''.join((language_prefix, '_', word.lower(), ' ', sentence_id))


def read_vocab(lines, thr):
    vocab = Counter()
    for line in lines:
        vocab.update(Counter(line.split('\t')[1].split(' ')))
    return dict([(token, count) for token, count in vocab.items() if count >= thr])

if __name__ == '__main__':
    main()

