#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function

from docopt import docopt
import sys
from os import path
import re
import clr
from sktagger import tag as tag_sk, init_tagger as init_sk_lemmatizer
sys.path.append(path.join(path.dirname(path.realpath(__file__)), 'Obeliks'))
clr.AddReference('PosTagger')
from PosTagger import PartOfSpeechTagger as SloveneLemmatizer
from PosTagger import Corpus as SloveneCorpus

sent_split_pat = re.compile(r' ?\$ \$ \$ \$ ?')

sk_lemmatizer = None
sl_lemmatizer = SloveneLemmatizer()

BATCH_SIZE = 5000


def main():
    args = docopt("""
    Lemmatizes the TSV format of bilingual data in Slovak and Slovene languages.

    Usage:
        tsv_lemmatize.py [options] <sk_lem_file> <sl_lem_file> <in_file> <out_file>

    Example:
        tsv_lemmatize.py data/tagger_model.sk data/sl_lem.bin europarl.tsv europarl_lemmatized.tsv
    """)

    in_filename = args['<in_file>']
    out_filename = args['<out_file>']
    sk_lem_model = args['<sk_lem_file>']
    sl_lem_model = args['<sl_lem_file>']

    print('Loading Slovak lemmatizer...')
    global sk_lemmatizer
    sk_lemmatizer = init_sk_lemmatizer(sk_lem_model)

    print('Loading Slovene lemmatizer...')
    sl_lemmatizer.LoadModels(None, sl_lem_model);

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
                if rec_num % BATCH_SIZE == 0:
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
    processed = tag_sk(longtext, sk_lemmatizer)

    sents = []
    for sent in processed:
        sents.append(' '.join([lemma.lower() for lemma, form in sent]).encode('utf-8') + ' ')

    text = 'sk\t' + ''.join(sents).strip(' $')
    text = re.sub(sent_split_pat, '\nsk\t', text)
    return text.split('\n')


def process_sentences_sl(sents, outfile):
    processed = []
    corpus = SloveneCorpus()
    for text in sents:
        corpus.LoadFromText(text.decode('utf-8'))
        sl_lemmatizer.Tag(corpus);
        lemmas = []
        for tagged in corpus.TaggedWords:
            lemmas.append((tagged.Lemma or tagged.Word).lower())
        processed.append('sl\t' + ' '.join(lemmas).encode('utf-8'))
    return processed


if __name__ == '__main__':
    main()

