import pandas as pd

def import_data(file:str):
    return pd.read_csv(file)


def drop_features(df, col_list_to_drop) :
    return df.drop(col_list_to_drop, axis=1)


def encode_target_5_cat(raw_grade:int) -> int:
    '''Encode FinalGrade into 5 categories instead of numeric value:    
    '''
    if raw_grade < 8:
        return 1
    elif raw_grade >=8 and raw_grade < 10:
        return 2
    elif raw_grade >= 10 and raw_grade < 12:
        return 3
    elif raw_grade >= 12 and raw_grade < 16:
        return 4
    elif raw_grade >=16 :
        return 5
