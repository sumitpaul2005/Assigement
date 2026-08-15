import pandas as pd
import numpy as np

# Q1. Download a small sample of your recent Zomato order history as a CSV (or create a mock CSV with restaurant names and order dates), then use pandas' duplicated() function to find and print any duplicate orders based on restaurant name and date.
"""
df = pd.read_csv("zomato_orders.csv")
print(df)

dup = df[df.duplicated(
    subset=['restaurant_name','order_date'],keep=False
)]
print(dup)
"""
# Q2. Given a list of Flipkart product reviews with some duplicate entries, use value_counts() in pandas to identify which review texts are repeated most often and display the top 3 most common duplicate reviews.
"""
df = pd.DataFrame(
    {'product': [
        'Samsung Galaxy',
        'Redmi Note 13',
        'OnePlus Nord',
        'Realme P3',
        'Samsung Galaxy',
        'iPhone 15',
        'Redmi Note 13',
        'OnePlus Nord',
        'Realme P3',
        'Samsung Galaxy',
        'iPhone 15',
        'Redmi Note 13'
    ],
    'review': [
        'Excellent product',
        'Good quality',
        'Excellent product',
        'Value for money',
        'Excellent product',
        'Amazing phone',
        'Good quality',
        'Excellent product',
        'Value for money',
        'Good quality',
        'Amazing phone',
        'Good quality'
    ]
    }
)
print(df)

df = df.value_counts(['review'])
print(df)
"""
# Q3. Create a DataFrame with mock data for Spotify playlists, including playlist names and creator usernames, where some rows are exact duplicates. Use drop_duplicates() to remove duplicate playlists and print the cleaned DataFrame.
"""
df = pd.DataFrame(
    {
    'playlist_name': [
        'Chill Vibes',
        'Workout Hits',
        'Bollywood Hits',
        'Chill Vibes',
        'Party Songs',
        'Workout Hits',
        'Lo-Fi Beats',
        'Bollywood Hits'
    ],
    'creator_username': [
        'user_101',
        'musiclover',
        'rahul23',
        'user_101',
        'dj_king',
        'musiclover',
        'lofi_girl',
        'rahul23'
    ]
}
)
print(df)

df = df.drop_duplicates(["playlist_name","creator_username"])
print(df)
"""

# Q4. Suppose you have a DataFrame of Instagram usernames where some entries have typos (like 'insta_queen', 'insta-queen', 'instaqueen'). Use the replace() function to standardize all these variants to 'instaqueen'.
"""
df = pd.DataFrame(
    {
    'username': [
        'insta_queen',
        'insta-queen',
        'instaqueen',
        'john123',
        'insta_queen',
        'insta-queen'
    ]
}
)
print(df)

df['username'] = df['username'].replace({
    'insta_queen': 'instaqueen',
    'insta-queen': 'instaqueen'
})
print(df)
"""

# Q5. You have a DataFrame column for payment status from a Paytm-like app with mixed values: 'Yes', 'yes', 'Y', 'No', 'no', 'N', and some with extra spaces. Write code to unify this column so all paid statuses become 1 and all unpaid statuses become 0, trimming whitespace and fixing capitalization where needed.<br><br><em><strong>Hint:</strong> Use str.strip(), str.lower(), and map/replace methods in pandas.</em>

df = pd.DataFrame(
    {
    'transaction_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'customer_name': ['Rahul', 'Priya', 'Amit', 'Neha', 'Ravi',
                      'Sneha', 'Karan', 'Pooja', 'Vikas', 'Anjali'],
    'transaction_amount': [500, 1200, 750, 300, 1500, 900, 450, 2000, 650, 800],
    'payment_status': ['Yes', ' yes ', 'Y', 'No', ' no ', 'N', 'YES', ' y ', 'No', ' yes']
}
)

print(df)

df['payment_status'] = df['payment_status'].str.strip().str.lower()

df['payment_status'] = df['payment_status'].replace({'yes':1,'y':1,'no':0,'n':0})
print(df)