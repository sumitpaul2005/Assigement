import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

"""
seaborn : statistics and visualizations

----> less code , dataset read 

teheme : 
set_theme(style="darkgrid")
sns.set_theme(style="whitegrid")
sns.set_theme(style="white")
sns.set_theme(style="dark")
sns.set_theme(style="ticks")


1. histogram : distribution of total_bill ,add kde = true
2. KDE : compare the smoker and  non-smoker distribution

4. box plot :bill amount differ between days
5. vilon plot : bill amount differ between days ,hue = "smoker"


"""

df = sns.load_dataset("tips")
print(df.head(29))

# 1. histogram : distribution of total_bill ,add kde = true

sns.histplot(
    data=df,
    x = 'total_bill',
    bins= 10,
    kde="true"
)
plt.show()


# 2. KDE : compare the smoker and  non-smoker distribution
"""
sns.set_theme(style="darkgrid")
sns.kdeplot(
    data= df,
    x="total_bill",
    hue="smoker"
)
plt.show()
"""

# 3. count plot : count the  customers visit today 
"""
sns.set_theme(style="dark")
sns.countplot(
    data= df,
    x="day",
    hue="smoker"
)
plt.show()
"""

# 4. box plot :bill amount differ between days
"""
sns.set_theme(style="ticks")
sns.boxplot(
    data=df,
    x="day",
    y="total_bill",
    hue="day"
)
plt.show()
"""

# 5. vilon plot : bill amount differ between days ,hue = "smoker"
"""
sns.set_theme(style="whitegrid")
sns.violinplot(
    data=df,
    x="day",
    y="total_bill",
    hue="smoker"
)
plt.show()
"""

# heat map   :
"""
df = df.corr(numeric_only=True)
sns.set_style(style="darkgrid")
sns.heatmap(
    data=df,
    annot=True,
    cmap="YlGnBu"
)

plt.show()
"""

# scatter plot :

"""sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="smoker"
)
plt.title("scatter plot of total_bill vs tip")
plt.show()
"""

# pair plot :
"""
sns.pairplot(
    data=df,
    hue="smoker",
    kind="reg",
    height=6,
    palette="Set2",
    vars=["total_bill","tip"]
)
plt.show()
"""