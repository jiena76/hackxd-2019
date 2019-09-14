import urllib.request
# import enchant #word dictionary/spell-check
from bs4 import BeautifulSoup
import re
import nltk
nltk.download('stopwords') #get only stopwords we need
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
    clean_tokens = tokens[:]

    for token in tokens:

        if token in stopwords.words('english') or not re.fullmatch('([A-Za-z])+(\.|\,|\:|\!\?)*', token):
            clean_tokens.remove(token)

    freq = nltk.FreqDist(clean_tokens)
    # for key, val in freq.items():
        # print(str(key) + ':' + str(val))
    freq.plot(20, cumulative=False)
