import nltk
from nltk.corpus import stopwords
import urllib
from bs4 import BeautifulSoup
from queue import PriorityQueue
#text = "Hello! Mr. Strange is cool? What is your name? It is pretty strange. Hello?"
stop_words = set(stopwords.words("english"))

extraWords = ['said', 'reading', 'story']

for w in extraWords:
    stop_words.add(w)


def goodWord(word):
    if (word == "function" or word == "false" or word.find("http") != -1 or word == "require"):
        return False
    if (word == "main" or word.find("www") != -1 or word.find('return') != -1 or word.find('margin') != -1):
        return False
    if (word.find("else") != -1 or word.find('true') != -1 or word.find('null') != -1):
        return False
    if (word.find(".") != -1 or word.find('/') != -1 or word.find('=') != -1):
        return False
    return True

url = "http://money.cnn.com/2018/01/12/pf/housing-prices-food-bank/index.html?iid=SF_LN"
fp = urllib.request.urlopen(url)
html = fp.read()
fp.close()

soup = BeautifulSoup(html, "html.parser")
div = soup.findAll('p')
words = []
for x in div:
    text = x.getText()
    words += nltk.word_tokenize(text)

filtered_sentence = [w for w in words if not w in stop_words]

def createCount(parsedWords):
    count = {}
    for w in parsedWords:
        if w != "." and w != "?" and w != "!":
            w = w.lower()
            if w in count:
                count[w] += 1
            else:
                count[w] = 1
    return count

wordDictionary = createCount(filtered_sentence)
q = PriorityQueue()
for key, value in wordDictionary.items():
    if len(key) > 3:
        if (goodWord(key)):
            q.put((-value, key))
for i in range(10):
    print(q.get())



"""
filtered_sentence = [w for w in words if not w in stop_words]



q = PriorityQueue()
for key, value in wordDictionary.items():
    if len(key) > 3:
        if (goodWord(key)):
            q.put((-value, key))
#for i in range(100):
    #print(q.get())
print(words)
"""
