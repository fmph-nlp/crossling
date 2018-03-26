import sys
from collections import defaultdict
from os.path import join


def main():
    path = sys.argv[1]
    outpath = sys.argv[2]
    l2e = defaultdict(list)

    with open(path) as fin:
        for line in fin:
            token = line.split()[0]
            language = token[:3]
            word = token[4:]
            new_line = word + line.strip()[4+len(word):]
            l2e[language].append(new_line)

    for language, embeddings in l2e.items():
        with open(join(outpath, language + '.vecs'), 'w') as fout:
            print >>fout, '\n'.join(embeddings),



if __name__ == '__main__':
    main()

