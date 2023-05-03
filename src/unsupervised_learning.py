from sklearn.decomposition import LatentDirichletAllocation, NMF
from gensim.models import Word2Vec

class UnsupervisedLearning:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        
    def train(self, X):
        if self.algorithm == "LDA":
            model = LatentDirichletAllocation(n_components=10, random_state=0)
        elif self.algorithm == "NMF":
            model = NMF(n_components=10, init='random', random_state=0)
        elif self.algorithm == "Word2Vec":
            sentences = [words for words in X]
            model = Word2Vec(sentences, min_count=1)
            model.train(sentences, total_examples=len(sentences), epochs=10)
        return model
