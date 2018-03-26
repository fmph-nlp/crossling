#!/bin/sh

# Convert multilingual corpus into word-sentenceid format
python2 hyperwords/bible2pairs.py 2 ${1} > ${1}/pairs

# Create the vocabulary
scripts/pairs2counts.sh ${1}/pairs > ${1}/counts
python2 hyperwords/counts2vocab.py ${1}/counts

# Run SGNS
mkdir ${1}/sgns
word2vecf/word2vecf -train ${1}/pairs -pow 0.75 -cvocab ${1}/counts.contexts.vocab -wvocab ${1}/counts.words.vocab -dumpcv ${1}/sgns/contexts -output ${1}/sgns/words -threads 4 -negative 1 -iters 100 -size 500

# Split vectors into individual languages
python2 hyperwords/multi2mono.py ${1}/sgns/words ${1}/sgns
for v in `ls ${1}/sgns/*.vecs`; do python2 hyperwords/text2numpy_nonewline.py ${v}; done

