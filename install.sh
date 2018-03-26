#!/bin/sh

# Install hyperwords
wget https://bitbucket.org/omerlevy/hyperwords/get/688addd64ca2.zip
unzip 688addd64ca2.zip
rm 688addd64ca2.zip
mv omerlevy-hyperwords-688addd64ca2/* .
rm -r omerlevy-hyperwords-688addd64ca2

# Add nonewline, bible2pairs, etc
mv xling/*.py hyperwords/.
chmod +x *.sh
chmod +x scripts/*.sh

# Install word2vecf
scripts/install_word2vecf.sh
cd word2vecf
make
cd ..

# Unzip corpora
mkdir bible
cd bible
wget https://bitbucket.org/omerlevy/xling_embeddings/downloads/edinburgh_bibles.zip
unzip edinburgh_bibles.zip
rm edinburgh_bibles.zip
cd ..
mkdir europarl
cd europarl
wget https://bitbucket.org/omerlevy/xling_embeddings/downloads/europarl.zip
unzip europarl.zip
rm europarl.zip
cd ..

