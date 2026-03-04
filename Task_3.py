# Challenge 3: The "Difficult" Multi-Step API Scraper
# Goal: Combining API calls, data cleaning, and timestamping.

# The Task: Use the CoinGecko API (or any public crypto/stock API) to fetch the current price of 3 coins: Bitcoin, Ethereum, and Solana.

# The Script must:

# Fetch the data for these 3 specific IDs.

# Flatten the JSON so the DataFrame has columns: Coin_Name, Price_USD, and Market_Cap.

# Add a new column called Last_Updated which contains the current system time (use datetime.now()).

# The Catch: If the API call fails or a coin is missing, the script should not crash; it should print an error message using the try/except logic learned on Day 2.


import pandas as pd
import requests
from datetime import datetime

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_market_cap=true"

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        records = []
        
        for coin in ["bitcoin", "ethereum", "solana"]:
            
            if coin in data:
                records.append({
                    "Coin_Name": coin.capitalize(),
                    "Price_USD": data[coin].get("usd"),
                    "Market_Cap": data[coin].get("usd_market_cap"),
                    "Last_Updated": datetime.now()
                })
            else:
                print(f"{coin} data not found in API response.")
        
        df = pd.DataFrame(records)
        
        print("\nCrypto Market Snapshot:\n")
        print(df)
    
    else:
        print("API request failed with status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request:", e)