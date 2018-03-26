# xling_embeddings: Simple Cross-Lingual Word Representations #

This repository contains the code and data introduced in:
"A Strong Baseline for Learning Cross-Lingual Word Embeddings from Sentence Alignments"
Omer Levy, Anders Søgaard, and Yoav Goldberg. EACL 2017.

To get started, download the repository and run *install.sh*. This will also download some multi-lingual corpora to your directory.

You can then create embeddings by running *create_embeddings.sh* with the directory of the desired multi-lingual corpus as an argument. For example:
./create_embeddings.sh bible
./create_embeddings.sh europarl

Finally, if you would like to replicate the results from the paper, use *evaluate.sh*. You can also modify the script that generated it (*generate_run_all.py*) to evaluate on any other type of embedding.

This implementation is based on the hyperwords project. Learn more at: https://bitbucket.org/omerlevy/hyperwords

