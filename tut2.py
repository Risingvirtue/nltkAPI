import nltk
from nltk.corpus import brown
words = brown.words(categories=["news", "art"])
print(words)
