import streamlit as st

def main_header():
    st.write("# Application de suivi et d'aide aux élèves")

    st.write('''
    #### Cette application permet de voir au travers d'un Dashboard les élèves qui nécessitent le plus d'attention.
    ''')


def main_dashboard(config_choice = 1):
    
    pass


def main_prediction(df_slider=""):
    st.write(df_slider)

    prediction = "necessite de l'attention" #en pratique il s'agit ici de la prediction du modele avec clf.predict(df_slider)
    st.subheader("L'etudiant choisi :")
    st.write(prediction)