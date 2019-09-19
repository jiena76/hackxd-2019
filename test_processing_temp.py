# for reading the webpage
import pandas as pd

import re
from nltk.stem import SnowballStemmer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import urllib.request
from bs4 import BeautifulSoup

import re  # regex matching

"""
Algorithm: 
Go through the webpage. Extract all the text   
"""
import nltk
# import list of stopwords (conjunctions, prepositions) and dictionary words
from nltk.corpus import stopwords
nltk.download('stopwords')

# import sentence splitting algorithm tools
nltk.download('punkt')
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument


link = 'https://www.facebook.com/legal/terms/update'

def predict_collection(attribute_file, link):
    df = pd.read_csv(attribute_file)

    """get all sentences with label "1", meaning these sentences imply that 
    the website is COLLECTING the specified attribute"""
    data_collecting_attribute = df.loc[df['Label'] == 1, 'Sentence']

    """get all sentences with label "1", meaning these sentences imply that 
    the website is NOT COLLECTING the specified attribute"""
    data_not_collecting_attribute =  df.loc[df['Label'] == 0, 'Sentence']


    #tag and tokenize sentences that collect specified attribute
    tagged_collecting_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=
    [str(i)]) for i, _d in enumerate(data_collecting_attribute)]

    #tag and tokenize sentences that DO NOT collect specified attribute
    tagged_not_collecting_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=
    [str(i)]) for i, _d in enumerate(data_not_collecting_attribute)]


    train_model(tagged_collecting_data, 'collecting2v.model')
    train_model(tagged_not_collecting_data, 'not_collecting2v.model')


def train_model(tagged_data, model_name): 
    max_epochs = 100
    vec_size = 20
    alpha = 0.025

    model = Doc2Vec(size=vec_size,
                    alpha=alpha, 
                    min_alpha=0.00025,
                    min_count=1,
                    dm =1)
    
    model.build_vocab(tagged_data)

    for epoch in range(max_epochs):
        print('iteration {0}'.format(epoch))
        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=model.iter)
        # decrease the learning rate
        model.alpha -= 0.0002
        # fix the learning rate, no decay
        model.min_alpha = model.alpha

    return model.save(model_name)






def assess_website(link):
    """
        Parameters: 
            link: the URL to the policy
        Returns: 
            clean_tokens: All sentences on the website 
    """
    # read the webpage
    response = urllib.request.urlopen(link)
    html = response.read()

    # take out sentences/tokens from webapge
    soup = BeautifulSoup(html, 'html5lib')
    text = soup.body.get_text(strip=True)
    sentences = (sent_tokenize(text))
    # print(sentences)

    # clean_tokens = sentences[:] #ALL sentences on webpage

    for words in sentences:
        # lazy way of removing sentences with just html in webpage
        if '{' in words or '}' in words or '[]' in words:
            sentences.remove(words)

    print(sentences)

    return sentences


if __name__ == "__main__":
    # assess_website(link)
    predict_collection('email_data.csv', link)
