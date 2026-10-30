import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# reg plot , catplot ,displot ,jointplot :
"""
sales =[100,250,150,400,500,600,750,800,900]
days =[1,2,3,4,5,6,7,8,9]

df = pd.DataFrame({"sales":sales,"days":days})
print(df)

sns.regplot(
    data=df,
    x=sales,
    y=days,
    scatter=True,
    line_kws={"color":"red"},
    ci=False    #Confidence interval
)
plt.show()
"""

# catplot
"""
df = sns.load_dataset("tips")
print(df)

sns.catplot(
    data=df,
    x="time",
    y="total_bill",
    hue="smoker",
    kind="bar",
    ci = False
)

plt.show()
"""

# displot
"""
df = sns.load_dataset("tips")

sns.displot(
    data=df,
    x="total_bill",
    hue="smoker",
    kind="kde"
)
plt.show()
"""

# jointplot

df = sns.load_dataset("tips")
plt.figure(figsize=(10,15))
sns.jointplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="smoker",
    kind="hist"
)
plt.show()

# EDA : Exploratory Data Analysis
"""
step :1 data read 
step :2 data cleaning ----> info,missing value , outlier , 
step :3 inslights 
       1. total  sales
       2. total profit 
       3. region wise sales , category wise sales , sub-category wise sales
       4. region wise profit , category wise profit , sub-category wise profit

step :4 matplotlib plot

"""