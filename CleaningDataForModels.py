import PullFromMongoDB
import numpy as np
import pandas as pd
import nltk
from nltk.stem import PorterStemmer
from nltk import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import seaborn as sns
import itertools
from nltk.corpus import wordnet
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report
import random
nltk.download('stopwords')
Stopwords=stopwords.words()
nltk.download('wordnet')
nltk.download('punkt')
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
nltk.download('averaged_perceptron_tagger')
wn_lemmas = set(wordnet.all_lemma_names())

def wordTokenize (sentence):
  finalList=list()
  newSentence=word_tokenize(sentence)
  for i in newSentence:
    if i in wn_lemmas:
      finalList.append(i)
  return finalList

def plot_sns(raw_data):
  data = np.array(raw_data)

  x = np.arange(len(raw_data))
  width = 0.2

  sns.axes_style('white')
  sns.set_style('white')

  ax = sns.barplot(x, data[:,0])
def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def getDataRow(listWords):
  returnList=[0] * 500
  for words in listWords:
   returnList=[a + b for a, b in zip(returnList, words)]
  return returnList

if __name__ == '__main__':
    documents = PullFromMongoDB.queryByIndexValue(100)
    arrayOfTokenizeSentences = list()
    #print(documents[0])
    sentences=list()
    for document in documents:
        sentences.append(document['attributes']['review'])
    #print(sentences[0])
    word_tokenize(sentences[0])
    for i in sentences:
        tokenized = word_tokenize(i)
        lema = list()
        for j in tokenized:
            lema.append(lemmatizer.lemmatize(j, pos=get_wordnet_pos(pos_tag(j)[0][0])))
        arrayOfTokenizeSentences.append(lema)

    wordDictionary = dict()
    for i in arrayOfTokenizeSentences:
        for j in i:
            if j in wordDictionary:
                wordDictionary[j] = wordDictionary[j] + 1
            else:
                add = {j: 1}
                wordDictionary.update(add)

    listOfValues = list()
    listOfWords = list()
    for i in (wordDictionary.values()):
        listOfValues.append(i)
    for i in (wordDictionary.keys()):
        listOfWords.append(i)
    listOfWords.reverse()
    listOfValues.reverse()
    print('Number of words:' + str(len(listOfWords)))

    dataframe = {'Word': listOfWords, 'Value': listOfValues}
    dataFrame = pd.DataFrame(dataframe)
    dataFrame = dataFrame.sort_values(by=['Value'], ascending=False)
    dataFrame = pd.DataFrame(dataFrame.head(20))

    sns.set_theme(style="whitegrid")
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(16, 6))
    ax = sns.barplot(x=dataFrame.Word, y='Value', data=dataFrame)
    plt.show()
