#for reading the webpage
import urllib.request
from bs4 import BeautifulSoup

#regex matching
import re

#import list of stopwords (conjunctions, prepositions)
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# open dataset with the URLs of existing policies
file_path = open('data_agreement_urls.txt', 'r')


count = 0
for line in file_path.readlines():
    count += 1
    # print("line is ", line)
    response = urllib.request.urlopen(line)
    html = response.read()
    # print(html)
    soup = BeautifulSoup(html, 'html5lib')
    text = soup.get_text(strip=True)
    # print(text)
    tokens = [t for t in text.split()]
    # print(tokens)

    sr = stopwords.words('english')
    clean_tokens = tokens[:] #ALL words on webpage
    important_words_only = tokens[:] #only key words (conjunctions and prepositions removed)
    
    for token in tokens:

        #remove any gibberish words from both lists
        if not re.fullmatch('([A-Za-z])+(\.|\,|\:|\!\?)*', token):
            clean_tokens.remove(token)
            important_words_only.remove(token)
            continue

        #if word is a conjunction or preposition, remove from important word array
        if token in stopwords.words('english'):
                important_words_only.remove(token)

    print(clean_tokens) 
    freq = nltk.FreqDist(clean_tokens)
    # for key, val in freq.items():
        # print(str(key) + ':' + str(val))
    freq.plot(20, cumulative=False)
