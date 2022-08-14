import streamlit as st
import pandas as pd

COLUMNS = ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 
'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 
'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences']

def sidebar_choose_student():
    st.sidebar.header("Choix de l'élève")
    student_id = st.sidebar.number_input('StudentID', 0)
    return student_id


def sidebar_student_characteristics(df_init, student_id):
        '''
        fonction qui permet de créer les widget afin de faire varier les caracteristiques actionable
        d'un éleve et voir si il peut s'ameliorer.
        df_init : caractéristiques initiales de l'eleve
        '''
        assert df_init.columns.to_list() == COLUMNS

        school = st.sidebar.select_slider("school",["GP","MS"], str(df_init.iloc[student_id,0]))
        studytime = st.sidebar.slider("studytime",1,4, int(df_init.iloc[student_id,13]))
        famsup = st.sidebar.select_slider("famsup",["no","yes"], df_init.iloc[student_id,16])
        paid = st.sidebar.select_slider("paid",["no","yes"], df_init.iloc[student_id,17])
        activities = st.sidebar.select_slider("activities",["no","yes"], df_init.iloc[student_id,18])
        internet = st.sidebar.select_slider("internet",["no","yes"], df_init.iloc[student_id,21])
        freetime = st.sidebar.slider("freetime",1,5, int(df_init.iloc[student_id,24]))
        goout = st.sidebar.slider("goout",1,5, int(df_init.iloc[student_id,25]))
        Dalc = st.sidebar.slider("Dalc",1,5, int(df_init.iloc[student_id,26]))
        Walc = st.sidebar.slider("Walc",1,5, int(df_init.iloc[student_id,27]))
        health = st.sidebar.slider("health",1,5, int(df_init.iloc[student_id,28]))
        abscences = st.sidebar.number_input('absences',0,100, int(df_init.iloc[student_id,29]))
        
        data_dict = {

            "school": school,
            "studytime": studytime,
            "famsup": famsup,
            "paid": paid,
            "activities":activities,
            "internet": internet, 
            "freetime": freetime,
            "goout":goout,
            "Dalc":Dalc,
            "Walc" : Walc,
            "health":health,
            "abscences":abscences
        }
        

        student_dict = {}
        for col in COLUMNS :
            if col not in data_dict.keys():
                student_dict[col] = df_init.loc[student_id,col]
            else : 
                student_dict[col] = data_dict[col] 


        student_char = pd.DataFrame(student_dict,index=[0])
        return student_char