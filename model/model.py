from json import load
import joblib

def load_model(saved_model):
    return joblib.load(open(saved_model, 'rb'))


