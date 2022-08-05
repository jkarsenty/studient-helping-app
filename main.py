import streamlit as st
import pandas as pd


st.write('''
# Application de suivi et d'aide aux élèves

Cette application permet de voir au travers d'un Dashboard les élèves qui nécessitent le plus d'attention.
''')

st.sidebar.header("Caractéristiques de l'élève")

def student_characteristics():
    '''
    fonction qui permet de faire varier les caracteristiques d'un eleve
        pour voir si il necessite plus d'attention.
    '''
    s_c_1 = st.sidebar.slider("name of char 1",0,10,3) #name, min_value, max_value, default_value
    s_c_2 = st.sidebar.slider("name of char 2",0,10,7)
    data_dict = {
        "s_c_1":s_c_1,
        "s_c_2":s_c_1
    }
    student_char = pd.DataFrame(data_dict,index=[0])
    return student_char

df = student_characteristics()
st.subheader("On cherche a savoir si cet eleve necessite une attention particuliere")
st.write(df)