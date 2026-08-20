import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from ydata_profiling import ProfileReport
import numpy as np
import sweetviz as sw
import dtale as dt


# Q1. Install the pandas-profiling library and generate a profile report for the 'Spotify Top 100 Songs' dataset (CSV available on Kaggle); open the HTML report and note any missing values or data type issues.
"""
df = pd.read_csv("spotify_songs.csv")
print(df)
print(df.head(10))
print(df.info())

profile = ProfileReport(
    df,
    title = "Spotify Top 100 Songs - Profile Report",
    explorative=True
)
profile.to_file("Spotify_top_100.html")
print("Profile Generate Successfully")
"""

# Q2. Use Sweetviz to create a comparison report between two CSV files: one containing Zomato restaurant data for Mumbai and another for Delhi. Briefly describe one key difference you spot in the visual report.<br><br><em><strong>Hint:</strong> Use analyze() for single file and compare() for two datasets.</em>
"""
mum = pd.read_csv("zomato_mumbai.csv")
delh = pd.read_csv("zomato_delhi.csv")

print(mum)
print(delh)

report = sw.compare(
    [mum, "Mumbai"],
    [delh, "Delhi"]
)

report.show_html("zomato_mumbai_delhi_report.html")
"""

# Q3. Open the Myntra product listings dataset in D-Tale, explore the interface, and use it to filter products with a price above ₹2000. Take a screenshot of the filtered view and note the number of such products.
"""
df = pd.read_csv("myntra_products.csv")
reprot = dt.show(df)
print((df["price"] > 2000).sum())
"""

# Q4. Given a pandas-profiling report for a Flipkart product reviews dataset, interpret and list two columns that may need cleaning or transformation before further analysis.<br><br><em><strong>Hint:</strong> Look for columns with high cardinality, missing values, or warnings in the report.</em>
"""
df = pd.read_csv("flipkart_reviews2.csv")

report = ProfileReport(
    df,
    title = "Flipkart_report",
    explorative=True
)

report.to_file("Flipkart_report.html")
print("Report Generated successfully")
"""

# Q5. Pick any one auto-EDA tool (pandas-profiling, Sweetviz, or D-Tale) and use ChatGPT or Copilot to generate a code snippet that loads a Swiggy food order CSV and produces a summary report. Run the code and attach the generated report or a screenshot as proof.

df = pd.read_csv("swiggy_orders.csv")

print(df.isna().sum())

report = sw.analyze(df)

report.show_html("Swiggy_order.html")
print("Successfully created reports")