


def main():
    corpus = 'bible'
    method = 'sgns'

    embedding_path = corpus + '/' + method

    # Alignment tasks
    run_alignment('graca/enfr', embedding_path, 'fr')
    run_alignment('graca/enes', embedding_path, 'es')
    run_alignment('graca/enpt', embedding_path, 'pt')
    run_alignment('hansards', embedding_path, 'fr')
    run_alignment('lambert', embedding_path, 'es')
    run_alignment('holmqvist', embedding_path, 'sv')
    run_alignment('cakmak', embedding_path, 'tr')
    # Mihalcea's data is reversed
    source_embedding, target_embedding = get_embeddings(embedding_path, 'ro')
    data_path = 'eval_data/mihalcea/'
    command = ' '.join(('python alignment_eval.py', target_embedding, source_embedding, data_path + 'alignment', data_path + 'test.ro', data_path + 'test.en'))
    run_task('mihalcea\\tro\\ten', command)
    run_task('mihalcea\\ten\\tro', command + ' R')

    # Wiktionary tasks
    run_wiktionary(embedding_path, 'fr')
    run_wiktionary(embedding_path, 'es')
    run_wiktionary(embedding_path, 'pt')
    run_wiktionary(embedding_path, 'ar')
    run_wiktionary(embedding_path, 'fi')
    run_wiktionary(embedding_path, 'he')
    run_wiktionary(embedding_path, 'hu')
    run_wiktionary(embedding_path, 'tr')


def get_embeddings(embedding_path, language):
    return embedding_path + '/en0.vecs', embedding_path + '/' + language + '0.vecs'


def run_alignment(task_name, embedding_path, language):
    source_embedding, target_embedding = get_embeddings(embedding_path, language)
    data_path = 'eval_data/' + task_name + '/'
    command = ' '.join(('python alignment_eval.py', source_embedding, target_embedding, data_path + 'alignment', data_path + 'test.en', data_path + 'test.' + language))
    run_task(task_name + '\\ten\\t' + language, command)
    run_task(task_name + '\\t' + language + '\\ten', command + ' R')


def run_wiktionary(embedding_path, language):
    source_embedding, target_embedding = get_embeddings(embedding_path, language)
    command = ' '.join(('python wiktionary_eval.py', source_embedding, target_embedding, 'eval_data/wiktionary/en-'+language+'-enwiktionary.txt'))
    run_task('WIKTIONARY\\ten\\t' + language, command)
    run_task('WIKTIONARY\\t' + language + '\\ten', command + ' R')


def run_task(task, command):
    print "result=`" + command + " | tr -d '[[:space:]]'`"
    print ''.join(('echo -e "', task, '\\t$result"'))


if __name__ == '__main__':
    main()
