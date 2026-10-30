# dataframe : 
"""
2 ways :
1. dict 
2. list 
"""

import pandas as pd
import numpy as np

# 1 Create dataframe using dict
"""
df = pd.DataFrame({
    "id" : [101,102,103,104,105],
    "name" : ["Sumit","Ved","Sujal","Ramesh","Suraj"],
    "age" : [21,22,25,26,24],
    "salary" : [2500,2360,1500,3650,2100]
})

print(df)
print(df.head(3))
print(df.tail(2))
print(df.describe())
print(df.info)
print(df.keys)
print(df.values)
print(df.index)
print(df.columns)
"""

# 2 Create dataframe using list
"""
df = pd.DataFrame([
    [101,"Sumit",22,50000],
    [102,"Ved",23,52000],
    [103,"Sujal",21,25000]
],columns=["id","name","age","salary"])
print(df)
print(df.head(3))
print(df.tail(2))
print(df.describe())
print(df.info)
print(df.index)
print(df.columns)
"""
"""
# ex :URL  :
df =pd.read_csv("https://github.com/dishant1123/ved_sumit_lib/blob/main/pandas/students.csv")
print(df.head())
"""

# Display the data from sql

import pymysql

conn = pymysql.connect(host="localhost",user="root",password="2005",port=3306,database="sumit")
df = pd.read_sql("SELECT * FROM doctor",conn)
print(df)
print(df.head(3))
print(df.tail(2))
print(df.describe())
print(df.info)
print(df.keys)
print(df.values)
print(df.index)
print(df.columns)
conn.close()
