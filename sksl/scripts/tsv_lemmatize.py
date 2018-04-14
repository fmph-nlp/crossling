#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function

from docopt import docopt
import sys
from sktagger import tag as tag_sk
import re

sent_split_pat = re.compile(r' ?\$ \$ \$ \$ ?')


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
                text = '$$ %s $$' % text
                if lang == 'sk':
                    texts['sk'].append(text)
                    if rec_num % 5000 == 0.5:
                        process_sentences_sk(texts['sk'], outfile)
                        texts['sk'] = []
                        print('Processed %d records' % rec_num, end='\r')
                        sys.stdout.flush()
                rec_num += 0.5
            
            for lang in ['sk']:
                process_sentences_sk(texts['sk'], outfile)
                texts['sk'] = []
            print('Processed %d records' % rec_num, end='\r')
    
    
def process_sentences_sk(sents, outfile):
    longtext = ' '.join(sents)
    processed = tag_sk(longtext)
    
    sents = []
    for sent in processed:
        sents.append(' '.join([lemma for lemma, form in sent]).encode('utf-8') + ' ')
        
    text = 'sk\t' + ''.join(sents).strip(' $')
    text = re.sub(sent_split_pat, '\nsk\t', text)
    outfile.write(text + '\n')
                  
                    
if __name__ == '__main__':
    main()

