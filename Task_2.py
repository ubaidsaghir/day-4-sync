# Challenge 2: The API to DataFrame Pipeline
# Goal: Use the requests library and convert JSON to a structured table.

# The Task: Have the intern write a script that:

# Uses requests.get() to fetch data from a public API (e.g., the JSONPlaceholder API: https://jsonplaceholder.typicode.com/posts).

# Converts the JSON response into a list of dictionaries.

# Loads that list into a Pandas DataFrame.

# Filters the DataFrame to only show rows where the userId is equal to 1.

# Constraint: They must include a check for the API status code (e.g., response.status_code == 200) to ensure the request was successful before trying to process it.


import pandas as pd
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response= requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    
    user_1_posts = df[df["userId"]==1]
    print("Filteted Data (userId == 1):\n")
    print(user_1_posts)
    
else:
    print("API request failed with status code:", response.status_code)    