import numpy as np
import random

sales_data = np.loadtxt("retailcorp_sales_data.csv",delimiter=",",dtype=int,skiprows=1,usecols=(1,2,3,4,5))

                                            # ===Section 1===

"""
Q1. Write NumPy code to create a random integer array of shape (30, 5) with values between 50
and 500. Name it sales_data.
"""

# sales_data = np.random.randint(sales_data,size=(30,5))
# print(sales_data)

"""
Q2. What function would you use to check the shape, data type, and number of dimensions of
sales_data?
"""

# print("Shape : ",sales_data.shape)
# print("Data Type : ",sales_data.dtype)
# print("Dimensions : ",sales_data.ndim)

# """
# Q3. How many total sales values are stored in this array? Write the NumPy expression to find this.
# """

# total = sales_data.sum()
# print("Total Sales : ",total)

# """
# Q4. Extract the sales data for just the first product (column 0). What is the resulting shape?
# """

# first_product = sales_data[0:,0:1]
# print(first_product)
# print("Shape : ",first_product.shape)

# """
# Q5. Slice the data to get sales for days 10 to 20 (inclusive) for all products.
# """

# print(sales_data[10:21])


#                                             # === Section 2 ===


# """
# Q6. Calculate the total sales for each product across all 30 days.
# Hint: Sum along axis=0
# """

# print("Total All product : ",sales_data.sum(axis=0))

# """
# Q7. Find the average daily sales across all products combined.
# """

# print("Average Daily Sales : ",sales_data.mean(axis=1))

# """
# Q8. Which product had the highest total sales? Write the NumPy code to find its index.
# Hint: np.argmax()
# """

# sum = sales_data.sum(axis=0)
# max = np.argmax(sum)
# print("Highest total sales : ",max)

# """
# Q9. Find the standard deviation of sales for each product. What does a high std dev indicate?
# """

# s = sales_data.std(axis=0)
# print("Standard Deviation : ",s)
# print("Highest Std is : ",np.argmax(s))

# """
# Q10. Calculate the median daily sales for the entire dataset.
# """

# print("Mean of daily sales is : ",np.median(sales_data,axis=1))

# """
# Q11. Find the minimum and maximum sales values recorded in the entire dataset.
# """

# print("Maximum sales : ",np.max(sales_data))
# print("Minimum sales : ",np.min(sales_data))


#                                             # === Section 3 ===


# """
# Q12. Write code to find all days where sales of Product 3 exceeded 300 units.
# """

# p3 = sales_data[sales_data[:, 2] > 300, 2]
# print(p3)

# """
# Q13. How many days had total sales (across all products) greater than 1500?
# Hint: Use np.sum() on a boolean mask
# """

# a = np.sum(sales_data,axis=0)
# total = a > 1500
# print(a)
# print(np.sum(total))

# """
# Q14. Replace all sales values below 60 with 60 (treat these as the minimum threshold). Write the
# NumPy code.
# """

# sales_data = np.where(sales_data < 60,60,sales_data)

# print(sales_data)


"""
Q15. Find the indices (day numbers) where Product 1 had its top 5 highest sales days.
Hint: np.argsort()
"""
a = sales_data[:, 0]

top5 = np.argsort(a)[-5:][::-1]

print("Day Numbers:", top5 + 1)
print("Sales:", a[top5])


"""
Q16. Each product has a different profit margin: [0.2, 0.35, 0.15, 0.4, 0.25]. Multiply the sales array
by this margin array to get profit data. What NumPy feature makes this possible?
Hint: Broadcasting
"""

# margin = np.array([0.2,0.35,0.15,0.4,0.25])
# profit = sales_data * margin

# print(profit)

"""
Q17. Normalise the sales data for each product so that values range between 0 and 1.
Hint: (x - min) / (max - min) per column
"""

# min = np.min(sales_data,axis=0)
# max = np.max(sales_data,axis=0)

# x = sales_data - min

# y = max - min
# normalize_value = x / y

# print(normalize_value)


"""
Q18. Compute the percentage change in total daily sales from one day to the next.
Hint: np.diff()
"""

total = np.sum(sales_data,axis=1)
per = (np.diff(total) / total[:-1]) * 100
print("Percentage of Daily sales : ",np.round(per,2))


"""
Q19. Stack a new row representing forecast sales for Day 31: [200, 310, 150, 420, 280]. What
function would you use?
Hint: np.vstack()
"""
"""
sales_data = sales_data.reshape(30,5)
sales_data = [200,310,150,420,200]
stack = np.vstack(sales_data)
print(stack)
"""

"""
Q20. Reshape the entire sales_data array into a 1D array. How many elements does it contain?
"""

# sales_data = np.hstack(sales_data)
# print(sales_data.shape)
# print(sales_data.ndim)


"""
Q21. Which 3 days had the highest combined sales across all products? Write code to find them.
"""

total_sales = np.sum(sales_data, axis=1)

print("Total Sales Per Day:")
print(total_sales)

top3_days = np.argsort(total_sales)[-3:][::-1]

print("\nTop 3 Days :")
print(top3_days)

print("\nTop 3 Sales:")
print(total_sales[top3_days])

"""
Q22. Compute a 7-day rolling average for Product 2's sales using NumPy. (No pandas allowed!)
Hint: Use a loop with np.mean() on slices
"""

prod2 = sales_data[:,1:2]
print("\nProduct 2 : \n",prod2)

for i in range(len(prod2)-6):
    avg = np.mean(prod2[i:i+7])
    rolling_avg = np.array(avg).reshape(1)
    print(np.round(rolling_avg,2))


"""
Q23. The company wants to give a 10% bonus for every day a product exceeds 400 units.
Calculate total bonus units per product.
"""

sale = np.where(sales_data > 400,sales_data * 0.1,0)
print(sale)

total_prod = np.sum(sale,axis=0)
print("Total Bonus for each units : \n",total_prod)


"""
Q24. Compare the first 15 days vs last 15 days: which half had better average sales per product?
"""

first15 = np.mean(sales_data[:16],axis=0)
last15 = np.mean(sales_data[16:],axis=0)

print("Average of First 15 days : \n",np.round(first15,2))
print("Average of Last 15 days : \n",np.round(last15,2))

for i in range(len(first15)):
    if first15[i] > last15[i]:
        print(f"Product {i+1} : first 15 days is better sales")
    elif first15[i] < last15[i]:
        print(f"Product {i+1} : last 15 days is better sales")
    else:
        print(f"Product {i+1} : both have the same average")


"""
Q25. Save the final cleaned array to a file called cleaned_sales.npy and write code to reload it.
Hint: np.save() and np.load()
"""

np.save("cleaned_sales.npy",sales_data)

print("Array save successfully!!")

loaded_sales = np.load("cleaned_sales.npy")

print(loaded_sales)