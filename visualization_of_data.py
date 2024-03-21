import pandas as pd 
import matplotlib.pyplot as plt

indexes = ["^GSPC", "^N225", "^FTSE", "^HSI", "^AS51", "^BVSP", "^GDAXI", "^J203.JO"]

#read files
for index in indexes:
    file = f'{index}.csv'
    data = pd.read_csv(file, index_col=0, parse_dates=True)

    plt.plot(data.index, data['Close'], label=index)

plt.title('Historical Closing Prices of Major Indexes')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()

# Show plot
plt.show()    

