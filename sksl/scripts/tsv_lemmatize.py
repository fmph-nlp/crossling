#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function

from docopt import docopt
import sys
from nltk.tokenize import word_tokenize
from sktagger import tag as tag_sk
from lemmagen.lemmatizer import Lemmatizer as SloveneLemmatizer
import re

sent_split_pat = re.compile(r' ?\$ \$ \$ \$ ?')
sl_lemmatizer = SloveneLemmatizer()


def main():
    args = docopt("""
    Lemmatizes the TSV format of bilingual data in Slovak and Slovene languages.

    Usage:
        tsv_lemmatize.py [options] <in_file> <out_file>

    Example:
        tsv_lemmatize.py europarl.tsv europarl_lemmatized.tsv
    """)

    in_filename = args['<in_file>']
    out_filename = args['<out_file>']

    print('Lemmatizing...')

    rec_num = 0.5

    texts = { 'sk': [], 'sl': [] }

    with open(in_filename) as infile:
        with open(out_filename, 'w') as outfile:
            for line in infile:
                lang, text = line.split('\t')
                if lang == 'sk':
                    text = '$$ %s $$' % text

                texts[lang].append(text)
                if rec_num % 5000 == 0:
                    process_sentences(texts, outfile)
                    texts = { 'sk': [], 'sl': [] }
                    print('Processed %d records' % rec_num, end='\r')
                    sys.stdout.flush()

                rec_num += 0.5

            process_sentences(texts, outfile)
            print('Processed %d records' % rec_num, end='\r')


def process_sentences(sents, outfile):
    for lang in ('sk', 'sl'):
        if lang == 'sk':
            sents[lang] = process_sentences_sk(sents[lang], outfile)
        elif lang == 'sl':
            sents[lang] = process_sentences_sl(sents[lang], outfile)

    for line_sk, line_sl in zip(sents['sk'], sents['sl']):
        outfile.write(line_sk + '\n')
        outfile.write(line_sl + '\n')


def process_sentences_sk(sents, outfile):
    longtext = ' '.join(sents)
    processed = tag_sk(longtext)

    sents = []
    for sent in processed:
        sents.append(' '.join([lemma.lower() for lemma, form in sent]).encode('utf-8') + ' ')

    text = 'sk\t' + ''.join(sents).strip(' $')
    text = re.sub(sent_split_pat, '\nsk\t', text)
    return text.split('\n')


def process_sentences_sl(sents, outfile):
    processed = []
    for text in sents:
        tokens = word_tokenize(text.decode('utf-8'))
        lemmas = [sl_lemmatizer.lemmatize(tok).lower() for tok in tokens]
        processed.append('sl\t' + ' '.join(lemmas).encode('utf-8'))
    return processed


if __name__ == '__main__':
    main()

