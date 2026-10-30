# pandas : python  library , use data cleaing

"""
1.data  cleaning  
2.data analysis  :  tops 3 product 
3.join ,merge
4. read any dataset : xlsx ,csv,tsv,json.sql   

"""

import pandas as pd
import numpy as np

# Series
"""
d = pd.Series([10,20,30,10,40,50])
print(d)
print(type(d))

a = pd.Series(["sumit",10,20,"Ramesh",1.50,36.12])      # It will convert the data type in string data type beacuse the string data type is highest bits
print(a)

b = pd.Series({"ram":50,"sita":60})
print(b)

c = pd.Series([10,20,30,410,50],index=["sita","ram","raju","rina","geeta"])     # it will specify the index 
print(c)

e = pd.Series([10,20,30,40],dtype=float)
print(e)

"""

# head() , tail() , describe() , info() , describe(all)
"""
a=pd.Series({"ravan":88,'ram':np.nan,'sita':89,'sumit':78,'ved':56,'prakash':99})   # np.nan is used for none value entry in numpy
a["ram"] = 100
print(a.head())   # it print by default 5 entry if no arg is given
print(a.head(3))    # it will print the 3 entry

print(a.tail())     # it will print last 5 entry
print(a.tail(3))

print(a.dtype)
print(a.info())     # it will show the details
print(a.describe())
print(a.describe(include=all))
print(a.keys())
print(a.values)
print(a.item)
"""

# read csv file   : 
"""
a = pd.read_csv("Libraries/pandas/students.csv")
print(a)
print(a.tail(2))
print(a.head(2))
print(a.describe())
print(a.info())
print(a.keys())
"""

# tsv file : tab separated value 

b = pd.read_csv("Libraries/pandas/students_age.tsv",sep='\t')

print(b)
print(b.head())


# json file :

j = pd.read_json("Libraries/pandas/students.json")

print(j)