# Georgian Word2Vec

This is [Gensim](https://radimrehurek.com/gensim/) Word2Vec model trained on Georgian Wikipedia text corpus gathered from [Wikipedia dump file](https://dumps.wikimedia.org/kawiki/latest/kawiki-latest-pages-articles.xml.bz2).

### Requirements

You need Python 3.5 or later to run this project.

Code in this repository requires Gensim Python library to run.

```sh
$ pip install --upgrade gensim 
```

### Usage

1. Download pretrained weights from release page.
2. Unzip weights in project folder.

Example of getting word embedding:
```sh
$ python test_word_vector.py 
```

Example of getting word similarity using embeddings:
```sh
$ python test_similar_words.py 
```