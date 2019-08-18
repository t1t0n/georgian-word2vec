from gensim.corpora.wikicorpus import WikiCorpus
from gensim.models.word2vec import Word2Vec
import multiprocessing
import logging

# enable logging
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt= '%H:%M:%S', level=logging.INFO)

# load Wiki dump file
wiki = WikiCorpus('kawiki-latest-pages-articles.xml.bz2',
                  lemmatize=False, dictionary={})
sentences = list(wiki.get_texts())

# define training parameters
params = {'size': 200, 'window': 10, 'min_count': 10,
          'workers': max(1, multiprocessing.cpu_count() - 1), 'sample': 1E-3, 
          'iter': 5, 'sg':1, 'hs':1}

# train and save word2vec model
word2vec = Word2Vec(sentences, **params)
word2vec.save("georgian_word2vec.model")
