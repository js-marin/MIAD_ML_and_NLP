import pandas as pd
import joblib
import sys
import os

def predict_price(Year, Mileage, Model):

    RF = joblib.load(os.path.dirname(__file__) + '/proyecto_1.pkl')
    enc = joblib.load(os.path.dirname(__file__) + '/encoder.pkl')

    DF =pd.DataFrame({'Year':[Year], 'Mileage':[Mileage], 'Model':[Model]})

    DF_encoded = enc.transform(DF)

    price = RF.predict(DF_encoded)

    return price