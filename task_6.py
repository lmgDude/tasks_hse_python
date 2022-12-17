import pandas as pd

url1 = 'https://raw.githubusercontent.com/ksegorov/python_homework/main/var5/df.csv'
url2 = 'https://raw.githubusercontent.com/ksegorov/python_homework/main/var5/grades.csv'
df = pd.read_csv(url1)
df2 = pd.read_csv(url2)

df_new = df2.merge(right=df, how='inner')

df_new = df_new.dropna()

df_new[['Student_ID', 'Grade']] = df_new[['Student_ID', 'Grade']].astype('int64')
df_new = df_new[df_new['Grade'] < df_new['Grade'].mean()]

df_new = df_new.sort_values('Student_ID', ascending=False).reset_index(drop=True)

value = df_new.iat[0, 0]
