import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

class TextCorpus:
    def __init__(self, path):
        self.path = path
    
    def read_text(self):
        with open(self.path, 'r') as file:
            text = file.read()
        return text
    
    def clean_text(self, text):
        stop_words = set(stopwords.words('english'))
        words = nltk.word_tokenize(text.lower())
        words = [word for word in words if word.isalpha() and word not in stop_words]
        return words
