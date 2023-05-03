import re

class Preprocessing:
    def __init__(self):
        pass
    
    def remove_punctuations(self, text):
        cleaned_text = re.sub('[^\w\s]', '', text)
        return cleaned_text
    
    def stemming(self, words):
        stemmer = nltk.PorterStemmer()
        stemmed_words = [stemmer.stem(word) for word in words]
        return stemmed_words
