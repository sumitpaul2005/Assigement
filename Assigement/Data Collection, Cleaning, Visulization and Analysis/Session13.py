import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Q1. Load the 'tips' dataset from Seaborn and create a pairplot to quickly visualize relationships between all numeric variables.
"""
df = sns.load_dataset("tips")
print(df)

plt.figure(figsize=(10,15))
sns.set_theme(style="darkgrid")
sns.pairplot(
    data=df,
    hue="smoker",
    kind="reg",
    height=5,
    palette="Set2"
)
plt.show()
"""

# Q2. Using the 'flights' dataset from Seaborn, generate a heatmap showing the correlation between months and years based on the number of passengers.<br><br><em><strong>Hint:</strong> Use pivot_table to reshape the data before plotting the heatmap.</em>
"""
df = sns.load_dataset("flights")
print(df)
df = df.pivot_table(index="month",columns="year",values="passengers")
print(df)

sns.set_theme(style="white")
sns.heatmap(
    data=df,
    annot=True,
    cmap="YlGnBu"
)
plt.title("Number of Passengers by Month and Year")
plt.show()
"""

# Q3. Create a relplot using the 'fmri' dataset from Seaborn to visualize how the signal changes over time for different event types.
"""
df = sns.load_dataset("fmri")
print(df)

sns.set_theme(style="dark")
sns.relplot(
    data=df,
    x="timepoint",
    y="signal",
    hue="event",
)
plt.title("FMRI Signal Changes Over Time")
plt.show()

"""

# Q4. Pick any categorical column from the 'titanic' dataset (like 'class' or 'sex') and use catplot to display the survival rate for each group with confidence intervals.
"""
df = sns.load_dataset("titanic")
print(df)

sns.set_theme(style="darkgrid")
sns.catplot(
    data=df,
    x="pclass",
    y="survived",
    ci=True,
    hue="sex",
    kind="bar"
)
plt.title("Survival Rate by Passenger Class")
plt.show()
"""

# Q5. Use jointplot on the 'penguins' dataset to visualize the relationship between bill_length_mm and flipper_length_mm, and fit a regression line on the scatter plot.<br><br><em><strong>Hint:</strong> Set kind='reg' in jointplot for regression line.</em>

df = sns.load_dataset("penguins")
print(df)

sns.set_theme(style="ticks")
sns.jointplot(
    data=df,
    x="bill_length_mm",
    y="flipper_length_mm",
    kind="reg",
    color="green"
)
plt.show()