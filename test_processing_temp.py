#for reading the webpage
import urllib.request
from bs4 import BeautifulSoup

import re #regex matching

"""
Algorithm: 
Go through the webpage. Extract all the text   
"""
#import list of stopwords (conjunctions, prepositions) and dictionary words
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

#import sentence splitting algorithm
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

#for reading csv training data
import pandas as pd 

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

def predict_collection(attribute_file):
    df = pd.read_csv(attribute_file)

    #sentences that mean website collects attribute
    sentences_with_attrib = df.loc[df['Label'] == 1, 'Sentence']
    #sentences that meant website DOESN'T collect attribute
    sentences_not_attrib = df.loc[df['Label'] == 0, 'Sentence']

    module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/3" 
    embed = hub.Module(module_url)

    similarity_input_placeholder = tf.placeholder(tf.string, shape=(None))
    similarity_sentences_encodings = embed(similarity_input_placeholder)



def assess_website(link):
    """
        Parameters: 
            link: the URL to the policy
        Returns: 
            clean_tokens: All sentences on the website 
    """
    #read the webpage
    response = urllib.request.urlopen(link)
    html = response.read()

    #take out sentences/tokens from webapge
    soup = BeautifulSoup(html, 'html5lib')
    text = soup.body.get_text(strip=True)
    sentences = (sent_tokenize(text))
    # print(sentences) 

    clean_tokens = sentences[:] #ALL sentences on webpage
    
    for words in clean_tokens:
        #lazy way of removing sentences with just html in webpage
        if '{' in words and '}' in words or '[]' in words: 
            clean_tokens.remove(words) 
    
    print(clean_tokens) 

    return clean_tokens


if __name__== "__main__":
    assess_website('')
    assess_website('')
