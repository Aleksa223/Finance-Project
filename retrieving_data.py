import yfinance as yf
import pandas as pd

#Get the most important index from each continent
indexes = ["^GSPC", "^N225", "^FTSE", "^HSI", "^AS51", "^BVSP", "^GDAXI", "^J203.JO"]

index_data = {}

# Retrieve historical data for each index
for index in indexes:
    index_info = yf.Ticker(index)
    index_data[index] = index_info.history(period="max")

#Extract historical data into csv file
for index, data in index_data.items():
    filename = f"{index}.csv"
    data.to_csv(filename)
    print(f"{index} historical data has been saved to {filename}")