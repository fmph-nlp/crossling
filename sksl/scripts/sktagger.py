#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
from ufal_morphodita import *
from snktagset import ufal2snk

tagger_file = '/home/ifrag/projects/crossling/xling/sksl/scripts/data/tagger_model.sk'

def init_tagger(tagger_file):
    tagger = Tagger.load(tagger_file)
    if not tagger:
      sys.stderr.write("Cannot load tagger from file '%s'\n" % tagger_file)
      sys.exit(1)
    return tagger


def tag(text, tagger=None, morpho=None):
    if not tagger:
        tagger = init_tagger(tagger_file)
    forms = Forms()
    lemmas = TaggedLemmas()
    tokens = TokenRanges()
    tokenizer = tagger.newTokenizer()

    # Tag
    tokenizer.setText(text)
    t = 0
    while tokenizer.nextSentence(forms, tokens):
      tagger.tag(forms, lemmas)

      sentence = []
      for i in range(len(lemmas)):
        lemma = lemmas[i]
        token = tokens[i]
        form = text[token.start : token.start + token.length]
        possible_lemmas = TaggedLemmas()
        lf = lemma.lemma, form
        sentence.append(lf)
      yield sentence
      

def lemmatize(text):
    for s in tag(text):
        for lemma, form in s:
            yield lemma


if __name__=='__main__':
    text = u'buď fit. Je a to celé v riti bzskej. Idem domov.'
    for s in lemmatize(text):
        for w in s:
            lemma, form = w
            print 'lemma: %s  form: %s' % (lemma, form)

