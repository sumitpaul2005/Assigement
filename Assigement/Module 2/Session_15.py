import sqlite3

""" Q1. Install the sqlite3 module in Python and write a script to create a new database called foodie.db with a table Restaurants (id, name, cuisine, rating)."""

conn = sqlite3.connect("foodie")
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE RESTAURENTS (ID SMALLINT PRIMARY KEY, NAME VARCHAR(50), CUISINE VARCHAR(50),RATING SMALLINT)""")

# conn.commit()
# conn.close()

# print("Database and Restaurents table are created successfully")

""" Q2. Using sqlite3 in Python, insert three sample restaurants into the Restaurants table in foodie.db and write a query to fetch all restaurants with a rating above 4.0, then print their names."""

# cursor = conn.execute("""INSERT INTO RESTAURENTS VALUES(1,'PIZZA HUTS','ITALIAN',4.5),(2,'SPICE VILLA','INDIAN',3.5),(3,'BURGER HOUSE','AMERICAN',4.3) """)

# conn.commit()
# print("Data insert successfully")

# cursor = conn.execute("""SELECT * FROM RESTAURENTS WHERE RATING > 4.0""")
# show = cursor.fetchall()

# for i in show:
#     print(i)
# conn.close()

""" Q3. Write Python code to load all rows from the Restaurants table in foodie.db into a Pandas DataFrame and display the top 2 rows using DataFrame.head()."""

import pandas as pd

df = pd.read_sql("SELECT * FROM RESTAURENTS",conn)
print(df.head(2))


"""Q4. Add a new column 'delivery_charge' to your DataFrame, setting it to 50 for all restaurants, and then calculate a new column 'final_rating' as rating + (0.1 if cuisine is 'Italian').<br><br><em><strong>Hint:</strong> Use DataFrame.apply() or a lambda function for the conditional logic.</em>"""

df['delivery_charge'] = 50
print(df)

df["final_rating"] = df.apply(
    lambda row: row["RATING"] + 0.1 if row["CUISINE"] == "ITALIAN" else row["RATING"],
    axis=1
)
print(df)


"""Q5. Automate a daily summary: Write a Python script that connects to foodie.db, fetches all restaurants with rating above 4.5, loads them into a DataFrame, and saves the result as a CSV file named top_rated_restaurants.csv."""


df.to_csv("top_rated_restaurants.csv")

print("CSV file create successfully")
