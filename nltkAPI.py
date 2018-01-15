import sys
import nltk
from nltk.corpus import stopwords
import urllib
from bs4 import BeautifulSoup
from queue import PriorityQueue
#text = "Hello! Mr. Strange is cool? What is your name? It is pretty strange. Hello?"
stop_words = set(stopwords.words("english"))

extraWords = ['said', 'reading', 'story', 'news']

def addStopWords(extraWords):
    for w in extraWords:
        stop_words.add(w)

addStopWords(extraWords)
def getWordList(html):
    words = []
    for x in html: #for every content in p
        text = x.getText() #text w/o html
        words += nltk.word_tokenize(text) #parses into words
    filtered_sentence = [w for w in words if not w in stop_words] #remove stop_words
    return filtered_sentence

def createCount(parsedWords):
    count = {}
    for w in parsedWords:
        if w != "." and w != "?" and w != "!":
            w = w.lower() #make all lowercase
            if w in count:
                count[w] += 1
            else:
                count[w] = 1
    return count

def getTopTen(wordDictionary):
    q = PriorityQueue()
    w = []
    for key, value in wordDictionary.items():
        if len(key) > 3:
            q.put((-value, key))

    for i in range(5):
        word = q.get()
        print(word)
        #w += [q.get()[1]]
    return w


if (len(sys.argv) == 1):
    print("Please provide a url link")
else:
    url = sys.argv[1]
    fp = urllib.request.urlopen(url)
    html = fp.read()
    fp.close()
    soup = BeautifulSoup(html, "html.parser")
    div = soup.findAll('p')

    filteredWords = getWordList(div)
    wordDictionary = createCount(filteredWords)
    topTen = getTopTen(wordDictionary)
    #print()
