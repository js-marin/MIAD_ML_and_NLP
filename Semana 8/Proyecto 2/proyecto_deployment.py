import pandas as pd
import joblib
import sys
import os

def predict_genre(Plot):



    LR = joblib.load(os.path.dirname(__file__) + '/logistic.pkl')
    vect = joblib.load(os.path.dirname(__file__) + '/vectorizer.pkl')
    labels_enc = joblib.load(os.path.dirname(__file__) + '/labels.pkl')

    vectorized_plot  = vect.transform([Plot])

    predicted = LR.predict(vectorized_plot)

    pred_genre = labels_enc.inverse_transform(predicted)

   

    return pred_genre