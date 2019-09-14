#for reading the webpage
import urllib.request
from bs4 import BeautifulSoup

import re #regex matching
# import enchant #dictionary

#import list of stopwords (conjunctions, prepositions) and dictionary words
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

#for reading csv training data
import pandas as pd 


def process_data(dataset):
    # open dataset with the URLs of existing policies
    # file_path = open('website_policy_data.csv', 'r')
    data_frame = pd.read_csv(dataset)

    for index,row in data_frame.iterrows():
        #read the webpage
        response = urllib.request.urlopen(row['Links'])
        html = response.read()

        #take out words/tokens from webapge
        soup = BeautifulSoup(html, 'html5lib')
        text = soup.body.get_text(strip=True)
        tokens = [t for t in text.split()]

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

        #plotting 20 most frequent IMPORTANT words
        # freq = nltk.FreqDist(important_words_only)
        # freq.plot(20, cumulative=False)


def assess_website(url):
    response = urllib.request.urlopen(url)


if __name__== "__main__":
    process_data('website_policy_data.csv')
