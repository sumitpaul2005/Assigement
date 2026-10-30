import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("Seaborn\sample_superstore (1).csv")
print(df)
"""
1. histogram : distribution of total_bill ,add kde = true
2. KDE : compare the smoker and  non-smoker distribution

4. box plot :bill amount differ between days
5. vilon plot : bill amount differ between days ,hue = "smoker"
"""
# his = df.groupby(["Region"])["Profit"].sum()
# print(his)

# Histrogram
"""
sns.set_theme(style="dark")
sns.histplot(
    data= df,
    x="Profit",
    kde=True,
    bin=600
)
plt.show()
"""
"""
The histogram shows that **most profits are between 200 and 350**.
There are fewer records with very low or very high profits.
The **highest profit is around 350, so most profits are in the medium range.
"""

# KDE 
"""
sns.set_theme(style="ticks")
sns.kdeplot(
    data=df,
    x = "Sales",
    hue="Region"
)
plt.show()
"""
"""
The KDE plot shows the distribution of Sales for each Region.

Sales are mostly concentrated at lower values.
All regions have a similar overall sales pattern.
Some regions have slightly different peaks, showing where sales are more common.
Very high sales values occur less frequently.

Conclusion: Sales are mostly concentrated at lower values, and the sales distribution is fairly similar across the different regions.
"""

# Box plot
"""
sns.set_theme(style="white")
sns.boxplot(
    data= df,
    y="Sales",
    x="Region",
    hue="Category",
)
plt.title("Region vs Sales")
plt.show()
"""
"""
The box plot compares Sales across different Regions and Categories.

Sales vary across all regions.
Some categories have higher sales than others.
The West and East regions generally show higher sales values.
There are some outliers, meaning a few orders have unusually high sales.

Conclusion: Sales differ by both Region and Category, with some regions and categories showing higher sales and a few unusually high values.
"""

# Violine PLot
"""
sns.set_theme(style="whitegrid")
sns.violinplot(
    data= df,
    x="Segment",
    y="Discount",
    hue="Region"
)
plt.show()
"""

"""
The violin plot shows the distribution of Discount across different Segments and Regions.

Most discounts are concentrated at lower values.
The discount distribution is different across some regions.
All three segments have a similar overall discount range.
Some regions show more variation in discounts than others.

Conclusion: Discounts are generally low, and the discount pattern varies somewhat by Region, while the difference between Segments is not very large.
"""


# Heat :
"""
df = df.corr(numeric_only=True)
sns.set_theme(style="dark")
sns.heatmap(
    data=df,
    annot=True
)
plt.show()
"""

"""
The heatmap shows the correlation between numerical columns in the dataset.

A value close to +1 means a strong positive relationship.
A value close to -1 means a strong negative relationship.
A value close to 0 means little or no relationship.
Sales and Profit generally show a positive relationship.
Discount has a weaker relationship with Sales and Profit.

Conclusion: Sales and Profit have a noticeable positive relationship, while Discount has a weaker relationship with the other numerical variables.
"""


# Scatter Plot
"""
sns.set_theme(style="darkgrid")
sns.scatterplot(
    data=df,
    y="Unit Price",
    x="Sales",
    hue="Segment"
)
plt.show()
"""
"""
The scatter plot shows the relationship between Sales and Unit Price for different Segments.

Most products have low to medium unit prices.
Sales values are spread across a wide range.
There is no very strong relationship between Unit Price and Sales.
The different segments (Consumer, Corporate, Home Office) are mixed throughout the chart.

Conclusion: Sales do not appear to depend strongly on Unit Price alone.

"""
# Pare plot

sns.set_theme(style="whitegrid")
sns.pairplot(
    data=df,
    vars=["Sales","Discount"],
    palette="Sets2",
)
plt.show()

"""
The pairplot shows the relationship between Sales and Discount.

Most discounts are low, mainly around 0%–30%.
Sales values are spread over a wide range.
There is no clear strong relationship between Sales and Discount.
Higher discounts do not always result in higher sales.

Conclusion: Discount does not appear to have a strong direct effect on Sales in this dataset.
"""