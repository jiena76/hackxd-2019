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
   
"""
import nltk
# import list of stopwords (conjunctions, prepositions) and dictionary words
from nltk.corpus import stopwords
from nltk.corpus import wordnet 

# import sentence splitting algorithm tools
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument


link = 'https://www.facebook.com/legal/terms/update'

def download_packages():
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')

def predict_collection(attribute_file, link):
    df = pd.read_csv(attribute_file)

    attribute = attribute_file.split('/')[1]
    attribute = attribute.split('_')[0]

    #remove all stopwords from training data
    stop = stopwords.words('english')
    df['Sentences_Without_stopwords'] = df['Sentence'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

    """get all sentences with label "1", meaning these sentences imply that 
    the website is COLLECTING the specified attribute"""
    data_collecting_attribute = df.loc[df['Label'] == 1, 'Sentence']
    # print(data_collecting_attribute)

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

    model_collecting = Doc2Vec.load('collecting2v.model')
    model_not_collecting = Doc2Vec.load('not_collecting2v.model')

    #to find the vector of a document which is not in training data
    sentences = assess_website_for_attribute(link, attribute)

    #keeps track of how many sentences match collecting data or not
    collecting_count = not_collecting_count = 0 
    for i in sentences:

        #filter out stopwords (i.e. 'but', 'a', 'an', etc.) from sentence
        test_data = word_tokenize(i.lower())
        test_data = [w for w in test_data if not w in stop] 

        v_collect = model_collecting.infer_vector(test_data)
        v_not_collect =  model_not_collecting.infer_vector(test_data)

        # get most similar sentence from each model 
        collect_similarity = model_collecting.docvecs.most_similar(positive=[v_collect],topn=1)[0][1]
        not_collect_similarity = model_not_collecting.docvecs.most_similar(positive=[v_not_collect],topn=1)[0][1]

        #see if sentence is more similar to collecting-data sentence or not-collecting-data sentence
        if collect_similarity >= not_collect_similarity:
            collecting_count+=1
        else:
            not_collecting_count+=1

    if  not_collecting_count > collecting_count:
        return 'This website may collect ' + attribute + ', but it does not sell it to third-parties.'
    else:
        return 'This website gives ' + attribute + ' to third parties.'
    

def train_model(tagged_data, model_name): 
    max_epochs = 100
    vec_size = 20
    alpha = 0.025

    model = Doc2Vec(vector_size=vec_size,
                    alpha=alpha, 
                    min_alpha=0.00025,
                    min_count=1,
                    dm =1)
    
    model.build_vocab(tagged_data)

    for epoch in range(max_epochs):
        # print('iteration {0}'.format(epoch))
        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=5)
       
        # decrease the learning rate
        model.alpha -= 0.0002
        # fix the learning rate, no decay
        model.min_alpha = model.alpha

    return model.save(model_name)


def assess_website_for_attribute(link, attrib):
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

    for words in sentences[:]:
        # lazy way of removing sentences with just html in webpage
        if '{' in words or '}' in words or "[]" in words:
            sentences.remove(words)
            continue

        #if neither attribute nor any synonym exists in word, then remove sentence from collection.
        if not any(synonym in words.lower() for synonym in wordnet.synset(attrib + '.n.1').lemma_names()):
            sentences.remove(words)

    return sentences


if __name__ == "__main__":

    #UNCOMMENT IF YOU HAVE NOT DOWNLOADED NLTK PACKAGES
    # download_packages()

    print(predict_collection('data/email_data.csv', link))
    print(predict_collection('data/name_data.csv', link))
