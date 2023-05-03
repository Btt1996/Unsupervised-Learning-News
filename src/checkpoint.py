import pickle

class Checkpoint:
    def __init__(self, path):
        self.path = path
    
    def save(self, model):
        with open(self.path, 'wb') as file:
            pickle.dump(model, file)
    
    def load(self):
        with open(self.path, 'rb') as file:
            model = pickle.load(file)
        return model
