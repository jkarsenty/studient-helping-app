from data_treatment.preprocessing import import_data


DATA_FILE = "data/student_data.csv"

df = import_data(DATA_FILE)
print(df.head())

