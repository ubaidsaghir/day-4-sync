# Day-4

# Challenge 1: The "Sales Insights" Aggregator
# Goal: Master the groupby() and agg() functions.

# The Task: Provide this dataset of sales transactions. The intern must write a script that calculates two things:

# The total revenue per Category.

# The average quantity sold per Region.


# import pandas as pd

# sales_data = {
#     'Region': ['North', 'South', 'North', 'East', 'South', 'East'],
#     'Category': ['Electronics', 'Furniture', 'Electronics', 'Electronics', 'Furniture', 'Furniture'],
#     'Revenue': [1200, 800, 1500, 2100, 450, 700],
#     'Quantity': [3, 2, 4, 5, 1, 2]
# }
# df = pd.DataFrame(sales_data)

# # Requirement: Output a summary DataFrame showing Total Revenue by Category.\
    

import pandas as pd

sales_data = {
    'Region': ['North', 'South', 'North', 'East', 'South', 'East'],
    'Category': ['Electronics', 'Furniture', 'Electronics', 'Electronics', 'Furniture', 'Furniture'],
    'Revenue': [1200, 800, 1500, 2100, 450, 700],
    'Quantity': [3, 2, 4, 5, 1, 2]
}
df = pd.DataFrame(sales_data)    

total_revenue= df.groupby("Category")["Revenue"].sum()
print("The total revenue per Category:\n")
print(total_revenue)


average_quantity= df.groupby("Region")["Quantity"].mean()
print("The average quantity sold per Region:\n")
print(average_quantity)
