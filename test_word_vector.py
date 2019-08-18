from gensim.models.word2vec import Word2Vec

model = Word2Vec.load("georgian_word2vec.model")
print(model['ნიუტონი'])