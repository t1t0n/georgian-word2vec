from gensim.models.word2vec import Word2Vec

model = Word2Vec.load("georgian_word2vec.model")

newton = model.most_similar_cosmul(positive='ნიუტონი'.split(), topn=5,)
for ii, (word, score) in enumerate(newton):
    print("{}. {} ({:1.2f})".format(ii+1, word, score))