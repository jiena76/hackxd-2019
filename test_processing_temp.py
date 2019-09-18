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
from nltk.corpus import words

#import sentence splitting algorithm
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

#for reading csv training data
import pandas as pd 

import fnmatch
import os

def assess_website(link, file):
    """
        Parameters: 
            link: the URL to the policy
            file: the datafile of the attribute (i.e email, name) that 
                    we test if the website collects.  
        Returns:
            Prediction: a 1 (website collects attribute) or 0 (doesn't collect attribute)
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
    
    for words in sentences:
        #lazy way of removing sentences with just html in webpage
        if '{' in words and '}' in words or '[]' in words: 
            clean_tokens.remove(words)
    
    print(clean_tokens) 


if __name__== "__main__":
    assess_website('', 'email_data.csv')
    assess_website('', 'name_data.csv')
