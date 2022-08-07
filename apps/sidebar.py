import streamlit as st
import pandas as pd

def sidebar_choose_config():
    st.sidebar.header("Choix du modèle")
    config_choice = st.sidebar.number_input('Version de la configuration', 1, 3,1)
    return config_choice


def student_characteristics(df,config_choice:int=1):
        '''
        fonction qui permet de créer les widget pour faire varier les caracteristiques
        d'un eleve et voir si il necessite plus d'attention.
        '''

        if config_choice == 1 :
            "1 feature"
            col_list = ["absences"]
            # for c in col_list:
            #     df[c]
            # stu_char_list = [())]

        elif config_choice == 2 :
            "8 most correlated features"
            col_list = ['failures','absences','goout','schoolsup','age','higher','guardian','Dalc']
            stu_char_list = []

        elif config_choice == 3 :
            col_list = []
            stu_char_list = []


        # for i in range(len(col_list)):
        #     s_c_i = st.sidebar.slider()


        s_c_1 = st.sidebar.slider("name of char 1",0,10,3) #name, min_value, max_value, default_value
        s_c_2 = st.sidebar.slider("name of char 2",0,10,7)
        
        data_dict = {
            "s_c_1":s_c_1,
            "s_c_2":s_c_2
        }
        student_char = pd.DataFrame(data_dict,index=[0])
        return student_char


def sidebar_student_characteristics():
    st.sidebar.header("Caractéristiques de l'élève")
    st.sidebar.select_slider('Pick one', ['cats', 'dogs'])

    df_slider = ""
    
    return df_slider