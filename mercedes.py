import pandas as pd
import matplotlib.pyplot as plt

mercedes = pd.read_excel("./20230404_DataForPEAnalysis.xlsx",sheet_name="Daimler")
date = mercedes["Date"]
pe = mercedes["P/E Ratio"]
internal_return = mercedes["Internal Return"]
marketCapitalization = mercedes["Market Capitalization"]
profit = mercedes["Profit"]
stockPrice = mercedes["Mercedes-Benz"]


plt.title("Mercedes Stock Price")
plt.ylabel("Price per Stock")
plt.xlabel("Date")
plt.plot(date,stockPrice)
plt.show()


plt.title("Profit")
plt.ylabel("Profit in Bio.")
plt.xlabel("Date")
plt.plot(date,profit)
plt.show()

plt.title("P/E Ratio")
plt.ylabel("P/E Ratio")
plt.xlabel("Date")
plt.plot(date,pe)
plt.show()

plt.title("Market Capitalization")
plt.ylabel("Market Capitalization in Bio.")
plt.xlabel("Date")
plt.plot(date,marketCapitalization)
plt.show()

plt.title("Internal Return")
plt.ylabel("Internal Return")
plt.xlabel("Date")
plt.plot(date,internal_return)
plt.show()


