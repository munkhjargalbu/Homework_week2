#Task_1

import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
#1
df = pd.read_excel(r"D:\Python\Homework\Homework_week2\data.xlsx")
#2
# Using pandas
df[(df["age"]<27) & (df["gender"] == "F")]

#Using loops

mylist=[]
for index, row in df.iterrows():
    if row['age']>25 and row['gender']=='F':
        mylist.append(row)
len(mylist)

df1 = pd.DataFrame(mylist)
#3
# Using pandas

df[(df["age"]<23) & (df["gender"] == "M")]

#Using loops

mylist=[]
for index, row in df.iterrows():
    if row['age']<23 and row['gender']=='M':
        mylist.append(row)
len(mylist)

df1 = pd.DataFrame(mylist)                    


df.to_csv('D:\Python\Homework/TEST.csv')
df.to_json('D:\Python\Homework/TEST.json')

