import pandas as pd
import numpy as np
import pymysql

"""
Connect to a MySQL or PostgreSQL database using SQLAlchemy and pandas, then use pd.read_sql() to load the entire 'restaurants' table 
(imagine Zomato backend) into a DataFrame and display the first 5 rows.
"""

# conn = pymysql.connect(host="localhost",port=3306,user="root",database="ass",password="2005")
# df = pd.read_sql("SELECT * FROM restaurants",conn)
# print(df)
# print(df.head(5))

# conn.close()

"""
Use pd.read_sql_query() to fetch only the 'name' and 'rating' columns from a 'movies' table (think BookMyShow-like data) where rating is 
above 8, and print the resulting DataFrame.<br><br><em><strong>Hint:</strong> Write a custom SQL SELECT query as the first argument to pd.read_sql_query().</em>
"""

# conn = pymysql.connect(host="localhost",port=3306,user="root",database="ass",password="2005")
# df = pd.read_sql_query("SELECT * FROM movies",conn)

# print(df)
# name_rating = df[df["rating"] > 8]
# name_rating = name_rating.loc[:,["name","rating"]]
# print(name_rating)

"""
Read a JSON dataset from the URL https://jsonplaceholder.typicode.com/users using pandas, convert it into a DataFrame, and print the usernames column.<br><br><em>
<strong>Hint:</strong> Use pd.read_json() directly with the URL.</em>
"""

# df = pd.read_json("https://jsonplaceholder.typicode.com/users")
# print(df)

"""
You have two CSV files: 'orders.csv' (order_id, user_id, amount) and 'users.csv' (user_id, username). Load both into DataFrames using pathlib for file paths, 
then merge them on 'user_id' to show a combined table with username and amount.
"""

from pathlib import Path
df1 = pd.read_csv("orders.csv")
df2 = pd.read_csv("user.csv")

print(df1)
print(df2)

df = pd.merge(df1,df2,on="user_id")

print(df[["username","amount"]])

"""
Concatenate two DataFrames representing 'today_orders' and 'yesterday_orders' (each with columns: order_id, item, price), and display the combined DataFrame.<br><br><em>
<strong>Constraint:</strong> Use pd.concat() and reset the index after concatenation.</em>
"""

today_order = pd.DataFrame({
    "order_id" : [6,7,8,9,10],
    "item" : ["cpu","mouse","monitor","tv","washing machine"],
    "price" : [30000,200,50000,35000,20000]
})

yesterday_order = pd.DataFrame({
    "order_id" : [1,2,3,4,5],
    "item" : ["mobile","cover","headphone","dongle","iphone"],
    "price" : [30000,250,1000,700,200000]
})

combine_df = pd.concat([today_order,yesterday_order],ignore_index=True)

print(combine_df)