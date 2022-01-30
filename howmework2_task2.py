#Task_2

import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_excel(r"D:\Python\Homework\Homework_week2\data.xlsx")

df.iloc[17,2:5]

df.iloc[25:28,("firstname","age")]

df.groupby('gender')['salary'].mean()
df.groupby("gender")['salary'].max()
df.groupby("gender")['salary'].min()
df.groupby("gender")['age'].mean()

res = df.groupby(['gender','salary']) \
        .agg({'age': ["mean","max","min"], 'salary': ["mean","max","min"]})

      
# pivot table 
df
import numpy as np

table = pd.pivot_table(df, values=['salary'], index=['gender',], aggfunc=np.mean)
table = pd.pivot_table(df, values=['salary'], index=['gender',], aggfunc=np.max)
table = pd.pivot_table(df, values=['salary'], index=['gender',], aggfunc=np.min)
table = pd.pivot_table(df, values=['age'], index=['gender',], aggfunc=np.mean)
                   
print(table)


table = pd.pivot_table(df, values=['age','salary'], index=['gender'],
            aggfunc={'age': ["mean","max","min"], 'salary': ["mean","max","min"]})
