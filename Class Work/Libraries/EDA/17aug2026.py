"""
EDA : exploratory data analysis

step : 1 


"""

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("EDA\Sample - Superstore.csv",encoding="ISO-8859-1")
print(df.head(10))

# info ,describe  -----> understand the  data  

"""print(df.info())
print(df.describe())
"""

# missing value, outlier  -----> 
"""
print(df.isnull().sum())
"""
# outlier for sales : 
"""q1= df['Sales'].quantile(0.25)
q3 = df['Sales'].quantile(0.75)

IQR = q3 -q1 
print("IQR :",IQR)

lower_limit = q1 - 1.5 * IQR
upper_limit = q3 + 1.5 * IQR

print("lower limit :",lower_limit)
print("upper limit :",upper_limit)

outlier = df[(df['Sales'] < lower_limit) | (df['Sales'] > upper_limit)]
print(outlier)
"""
# box plot for outlier  fo sales :
"""
plt.boxplot(df['Sales'])
plt.show()"""

# slights : 

# 1. top 5 sub-category  wise profit  bar chart :
"""top_5 = df.groupby(['Sub-Category'])['Profit'].sum().sort_values(ascending=False).head(5)
print(top_5)

# top 5 sub-category  wise profit  bar chart :

plt.bar(top_5.index,top_5)
plt.title("Top 5 Sub-Category wise Profit")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")
plt.show()
"""
# 2. top 5 sub-category  wise sales  bar chart :

"""top_5 = df.groupby(['Sub-Category'])['Sales'].sum().sort_values(ascending=False).head(5)
print(top_5)
"""
# top 5 sub-category  wise profit  bar chart :

"""plt.bar(top_5.index,top_5)
plt.title("Top 5 Sub-Category wise Profit")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")
plt.show()
"""

# 3. sales profit  line 
"""
df = df.sort_values(["Sales"],ascending=False).head(10)
print(df)
plt.plot(
    df['Sales'],df["Profit"],color="red"
)

plt.title("Sales Profit Plot")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()
"""

# 4. category profit, region ,   ----> sales cat , region 
"""
cat_pro = df.groupby(["Category"])["Profit"].sum()
print(df)

plt.bar(cat_pro.index,cat_pro)
plt.title("Category wise Profit")
plt.xlabel("Category")
plt.ylabel("Profit")

for i,j in enumerate(cat_pro.values):
    plt.text(
        i,j+5,f"{j:.2f}",color="red",ha="center"
    )
plt.show()
"""

    # Profit wise region
"""  
reg = df.groupby(["Region"])["Profit"].sum()
print(reg)

plt.bar(reg.index,reg,color="green")
plt.title("Region wise Profit")
plt.xlabel("Region")
plt.ylabel("Profit")

for i,j in enumerate(reg.values):
    plt.text(
        i,j+5,f"{j:.2f}",color="red",ha="center"
    )
plt.show()
"""

# 5. month year day  wise  sales , profit    ----> to_datetime ----> order_date  
"""
df["Order Date"] = pd.to_datetime(df["Order Date"],format="%m/%d/%Y")
df["year"] = df["Order Date"].dt.year
df["month"] = df["Order Date"].dt.month
df["day"] = df["Order Date"].dt.day
day = df.groupby(["day"])["Profit"].sum()
print(df.sort_values(["year"])["Profit"])
print(df.sort_values(["month"])["Profit"].sum())
print(day)

df = df.sort_values(["Profit"],ascending=False).head(10)
df = df.sort_values(["Sales"],ascending=False).head(10)

plt.figure(figsize=(10,15))
plt.subplot(2,3,1)
plt.bar(df["year"],df["Profit"])

plt.subplot(2,3,2)
plt.plot(df["month"],df["Profit"])

plt.subplot(2,3,3)
plt.plot(df["day"],df["Profit"])

plt.subplot(2,3,4)
plt.bar(df["year"],df["Sales"])

plt.subplot(2,3,5)
plt.plot(df["month"],df["Sales"])

plt.subplot(2,3,6)
plt.plot(df["day"],df["Sales"])

plt.show()
"""
# 6. discount ,sales  ----> graph  ----> relaition  -----> heatmap 
"""
sales_dis = df.loc[:,["Sales","Discount"]]
sales_dis = sales_dis.corr(numeric_only=True)
print(sales_dis)
sns.heatmap(
    data=sales_dis,
    annot=True
    )
plt.show()
"""
# 7. customer wise profit  , sales  

cust_pro = df.groupby(["Customer Name"])["Profit"].sum().sort_values(ascending=False).head(5)
print(cust_pro)

plt.plot(
    cust_pro.index,cust_pro
)
plt.show()

# 8. product wise profit  , sales
"""
import ydata_profiling as ydp

report = ydp.ProfileReport(df, title="Superstore Analysis Report")
report.to_file("Superstore_analysis_report.html")

import sweetviz as sv

report = sv.analyze(df)
report.show_html("sweet_report.html")
"""