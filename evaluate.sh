result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/fr0.vecs eval_data/graca/enfr/alignment eval_data/graca/enfr/test.en eval_data/graca/enfr/test.fr | tr -d '[[:space:]]'`
echo -e "graca/enfr\ten\tfr\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/fr0.vecs eval_data/graca/enfr/alignment eval_data/graca/enfr/test.en eval_data/graca/enfr/test.fr R | tr -d '[[:space:]]'`
echo -e "graca/enfr\tfr\ten\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/es0.vecs eval_data/graca/enes/alignment eval_data/graca/enes/test.en eval_data/graca/enes/test.es | tr -d '[[:space:]]'`
echo -e "graca/enes\ten\tes\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/es0.vecs eval_data/graca/enes/alignment eval_data/graca/enes/test.en eval_data/graca/enes/test.es R | tr -d '[[:space:]]'`
echo -e "graca/enes\tes\ten\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/pt0.vecs eval_data/graca/enpt/alignment eval_data/graca/enpt/test.en eval_data/graca/enpt/test.pt | tr -d '[[:space:]]'`
echo -e "graca/enpt\ten\tpt\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/pt0.vecs eval_data/graca/enpt/alignment eval_data/graca/enpt/test.en eval_data/graca/enpt/test.pt R | tr -d '[[:space:]]'`
echo -e "graca/enpt\tpt\ten\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/fr0.vecs eval_data/hansards/alignment eval_data/hansards/test.en eval_data/hansards/test.fr | tr -d '[[:space:]]'`
echo -e "hansards\ten\tfr\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/fr0.vecs eval_data/hansards/alignment eval_data/hansards/test.en eval_data/hansards/test.fr R | tr -d '[[:space:]]'`
echo -e "hansards\tfr\ten\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/es0.vecs eval_data/lambert/alignment eval_data/lambert/test.en eval_data/lambert/test.es | tr -d '[[:space:]]'`
echo -e "lambert\ten\tes\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/es0.vecs eval_data/lambert/alignment eval_data/lambert/test.en eval_data/lambert/test.es R | tr -d '[[:space:]]'`
echo -e "lambert\tes\ten\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/sv0.vecs eval_data/holmqvist/alignment eval_data/holmqvist/test.en eval_data/holmqvist/test.sv | tr -d '[[:space:]]'`
echo -e "holmqvist\ten\tsv\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/sv0.vecs eval_data/holmqvist/alignment eval_data/holmqvist/test.en eval_data/holmqvist/test.sv R | tr -d '[[:space:]]'`
echo -e "holmqvist\tsv\ten\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/tr0.vecs eval_data/cakmak/alignment eval_data/cakmak/test.en eval_data/cakmak/test.tr | tr -d '[[:space:]]'`
echo -e "cakmak\ten\ttr\t$result"
result=`python alignment_eval.py bible/sgns/en0.vecs bible/sgns/tr0.vecs eval_data/cakmak/alignment eval_data/cakmak/test.en eval_data/cakmak/test.tr R | tr -d '[[:space:]]'`
echo -e "cakmak\ttr\ten\t$result"
result=`python alignment_eval.py bible/sgns/ro0.vecs bible/sgns/en0.vecs eval_data/mihalcea/alignment eval_data/mihalcea/test.ro eval_data/mihalcea/test.en | tr -d '[[:space:]]'`
echo -e "mihalcea\tro\ten\t$result"
result=`python alignment_eval.py bible/sgns/ro0.vecs bible/sgns/en0.vecs eval_data/mihalcea/alignment eval_data/mihalcea/test.ro eval_data/mihalcea/test.en R | tr -d '[[:space:]]'`
echo -e "mihalcea\ten\tro\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/fr0.vecs eval_data/wiktionary/en-fr-enwiktionary.txt | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\ten\tfr\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/fr0.vecs eval_data/wiktionary/en-fr-enwiktionary.txt R | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\tfr\ten\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/es0.vecs eval_data/wiktionary/en-es-enwiktionary.txt | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\ten\tes\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/es0.vecs eval_data/wiktionary/en-es-enwiktionary.txt R | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\tes\ten\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/pt0.vecs eval_data/wiktionary/en-pt-enwiktionary.txt | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\ten\tpt\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/pt0.vecs eval_data/wiktionary/en-pt-enwiktionary.txt R | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\tpt\ten\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/ar0.vecs eval_data/wiktionary/en-ar-enwiktionary.txt | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\ten\tar\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/ar0.vecs eval_data/wiktionary/en-ar-enwiktionary.txt R | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\tar\ten\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/fi0.vecs eval_data/wiktionary/en-fi-enwiktionary.txt | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\ten\tfi\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/fi0.vecs eval_data/wiktionary/en-fi-enwiktionary.txt R | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\tfi\ten\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/he0.vecs eval_data/wiktionary/en-he-enwiktionary.txt | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\ten\the\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/he0.vecs eval_data/wiktionary/en-he-enwiktionary.txt R | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\the\ten\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/hu0.vecs eval_data/wiktionary/en-hu-enwiktionary.txt | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\ten\thu\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/hu0.vecs eval_data/wiktionary/en-hu-enwiktionary.txt R | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\thu\ten\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/tr0.vecs eval_data/wiktionary/en-tr-enwiktionary.txt | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\ten\ttr\t$result"
result=`python wiktionary_eval.py bible/sgns/en0.vecs bible/sgns/tr0.vecs eval_data/wiktionary/en-tr-enwiktionary.txt R | tr -d '[[:space:]]'`
echo -e "WIKTIONARY\ttr\ten\t$result"
