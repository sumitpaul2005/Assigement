import pandas as pd
import sqlite3

""" Q1. Import a CSV file of food delivery orders (with columns like order_id, restaurant_name, customer_name, order_amount, order_date) into a new SQL table named FoodOrders using your database tool of choice. """

df = pd.read_csv("Food delivery orders.csv")

print(df)

conn = sqlite3.connect("foodie")
cursor = conn.cursor()

df.to_sql("FoodOrder",
          conn,
          if_exists='replace',
          index=False)

print("Table created successfully")

food = pd.read_sql("SELECT * FROM FoodOrder",conn)

print(food)



""" Q2. Write SQL statements to create a table called TopSongs with columns: song_id, song_title, artist, streams, and release_date, then insert at least 5 records representing popular tracks from Spotify. """

# cursor.execute("CREATE TABLE TOPSONGS (SONGID SMALLINT PRIMARY KEY, SONG_TITLE VARCHAR(50), ARTIST VARCHAR(50), STREAMS BIGINT, RELEASE_DATE DATE)")

# print("Table created successfully")

# cursor.execute("""INSERT INTO TOPSONGS (SONGID,SONG_TITLE, ARTIST, STREAMS, RELEASE_DATE) VALUES(1, "Blinding Lights", 'The Weeknd', 4500000000, '2019-11-29')""")
# cursor.execute("""INSERT INTO TOPSONGS (SONGID,SONG_TITLE, ARTIST, STREAMS, RELEASE_DATE) VALUES(2, 'Shape of You', 'Ed Sheeran', 4200000000, '2017-01-06')""")
# cursor.execute("""INSERT INTO TOPSONGS (SONGID,SONG_TITLE, ARTIST, STREAMS, RELEASE_DATE) VALUES(3, 'Dance Monkey', 'Tones and I', 3800000000, '2019-05-10')""")
# cursor.execute("""INSERT INTO TOPSONGS (SONGID,SONG_TITLE, ARTIST, STREAMS, RELEASE_DATE) VALUES(4, 'Someone You Loved', 'Lewis Capaldi', 3000000000, '2018-11-08')""")
# cursor.execute("""INSERT INTO TOPSONGS (SONGID,SONG_TITLE, ARTIST, STREAMS, RELEASE_DATE) VALUES(5, 'As It Was', 'Harry Styles', 2800000000, '2022-04-01')""")

# print("INSERT RECORDS SUCCESSFULLY")

# food = cursor.execute("SELECT * FROM TOPSONGS")
# for i in food:
#     print(i)


""" Q3. Write an SQL query to find the top 3 customers who ordered the most from the FoodOrders table based on total order_amount, and display their names and total spent."""

# top3 = df.sort_values(by=['order_amount'], ascending=False)[['restaurant_name','order_amount']]
# print(top3.head(3))


""" Q4. Generate a product performance report by writing an SQL query that lists each restaurant_name from FoodOrders, the number of orders, and the total order_amount, ordered by total order_amount descending.<br><br><em><strong>Hint:</strong> Use GROUP BY and ORDER BY clauses.</em> """

report = (
    df.groupby("restaurant_name")
      .agg(
          number_of_orders=("order_id", "count"),
          total_order_amount=("order_amount", "sum")
      )
      .sort_values("total_order_amount", ascending=False)
      .reset_index()
)

print(report)


"""Q5. Create an SQL query that calculates two KPIs for the FoodOrders table: (1) average order_amount and (2) total number of unique customers, and format the output for dashboard display (two columns: kpi_name, kpi_value). """

average_order_amount = round(df["order_amount"].mean(), 2)
total_unique_customers = df["customer_name"].nunique()

kpi_report = pd.DataFrame({
    "kpi_name": [
        "Average Order Amount",
        "Total Unique Customers"
    ],
    "kpi_value": [
        average_order_amount,
        total_unique_customers
    ]
})

print(kpi_report)