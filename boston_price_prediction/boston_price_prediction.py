import pickle
import numpy as np

class BostonPricePrediction:
    def __init__(self):
        self.model = pickle.load(open('boston_lr_ml_model.sav','rb'))

    def predict(self, features):
        try:
            data = [[float(features['indus']),
            float(features['nox']),
            float(features['age']),
            float(features['tax']),
            float(features['rm']),
            float(features['ptratio']),
            float(features['lstat'])]]
            return self.model.predict(data)
        except:
            pass