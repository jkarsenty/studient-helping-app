import numpy as np
import streamlit as st

def main_header():
    st.write("# Application de suivi et d'aide aux élèves")

    st.write('''
    #### Cette application permet de voir au travers d'un Dashboard les élèves qui nécessitent le plus d'attention.
    ''')


def main_dashboard():
    
    pass


def main_prediction(df_slider, df_init, model):
    st.write(df_slider)

    prediction_rgs = np.round(model.predict(df_slider))
    st.subheader("L'etudiant choisi :")
    st.write(prediction_rgs)