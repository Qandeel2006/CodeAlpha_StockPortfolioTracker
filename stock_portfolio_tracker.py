# stock prices (fixed)
import os
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
    "META": 300,
    "NFLX": 450,
    "NVDA": 480,
    "AMD": 110,
    "INTC": 35,
    "IBM": 150,
    "ORCL": 115,
    "ADBE": 520,
    "UBER": 60,
    "DIS": 95,
    "NKE": 105,
    "KO": 60,
    "PEPSI": 170,
    "WMT": 160,
    "JPM": 150,
}
print("Available stocks and prices:")
for name in prices:
    print(name, "-", "$" + str(prices[name]))
total = 0
result = ""   # text we will save in the file
while True:
    name = input("\nEnter stock name (or type 'done' to finish): ").upper()
    if name == "DONE":
        break
    if name in prices:
        quantity = int(input("Enter quantity: "))
        value = prices[name] * quantity
        total = total + value
        line = name + ": " + str(quantity) + " x $" + str(prices[name]) + " = $" + str(value)
        print(line)
        result = result + line + "\n"
    else:
        print("Stock not found, try again.")
print("\nTotal investment: $" + str(total))
result = result + "Total investment: $" + str(total)
# save to a text file (in the same folder as this script)
folder = r"D:\Qandeel-Qudsia\internship"

# make the folder if it does not exist
if not os.path.exists(folder):
    os.makedirs(folder)
path = os.path.join(folder, "portfolio.txt")
file = open("portfolio.txt", "w")
file.write(result)
file.close()
print("Saved to portfolio.txt")
print("Saved in:", os.getcwd())