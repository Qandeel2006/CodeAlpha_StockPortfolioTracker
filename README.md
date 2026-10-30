<h1 align="center">📈 Stock Portfolio Tracker</h1>

<p align="center">
  <b>Work out the total value of your stocks with a simple Python script.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/CodeAlpha-Task%202-6C47FF" alt="CodeAlpha">
  <img src="https://img.shields.io/badge/Level-Beginner-orange" alt="Level">
</p>

---

## 💡 About

This is **Task 2** of my [CodeAlpha](https://www.codealpha.tech) Python Programming Internship.
You enter the stocks you own and how many shares you have. The program adds everything up and shows your **total investment**.

## ✨ Features

- 📝 Choose from **20 stocks** and enter any quantities
- 💰 Shows the value of each stock and the total
- 💾 Saves the result to `portfolio.txt` in a folder you choose (set in the code) and prints the full path
- ⚠️ Tells you if a stock name is not in the list

## 💵 Stock Prices

The prices are fixed inside the code (no internet needed). There are **20 stocks** to choose from:

| Stock | Price | Stock | Price |
|-------|-------|-------|-------|
| AAPL  | $180  | NKE   | $105  |
| TSLA  | $250  | DIS   | $95   |
| GOOGL | $140  | UBER  | $60   |
| MSFT  | $330  | ADBE  | $520  |
| AMZN  | $125  | ORCL  | $115  |
| META  | $300  | IBM   | $150  |
| NFLX  | $450  | INTC  | $35   |
| NVDA  | $480  | AMD   | $110  |
| KO    | $60   | PEPSI | $170  |
| WMT   | $160  | JPM   | $150  |

> These are made-up example prices for practice, not real market prices. You can add your own stocks by adding a new line to the `prices` dictionary in the code.

## 🖥️ Example

```text
Enter stock name (or type 'done' to finish): AAPL
Enter quantity: 2
AAPL: 2 x $180 = $360
Enter stock name (or type 'done' to finish): TSLA
Enter quantity: 3
TSLA: 3 x $250 = $750
Enter stock name (or type 'done' to finish): done
Total investment: $1110
Saved to: D:\Qandeel-Qudsia\internship\portfolio.txt
```

## 📂 Where Is the File Saved?

The result is saved to `portfolio.txt` in the folder set inside `stock_portfolio_tracker.py`:

```python
folder = r"D:\Qandeel-Qudsia\internship"
```

**To save it somewhere else**, change the path between the quotes (keep the `r` before the first quote), for example:

```python
folder = r"C:\Users\YourName\Documents"
```

The folder is created automatically if it does not exist, and the full path is printed when the program finishes.

## ⚙️ Getting Started

**Requirements:** Python 3 (nothing else to install)

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_StockPortfolioTracker.git
cd CodeAlpha_StockPortfolioTracker
python stock_portfolio_tracker.py
```

> On some computers the command is `python3` instead of `python`.

## 🧠 Concepts Used

| Concept | Where it is used |
|---------|------------------|
| Dictionary | Storing the stock prices |
| Input / output | Asking for stocks and showing results |
| Arithmetic | Price × quantity, and the total |
| File handling | Saving the result to `portfolio.txt` |

## 📁 Project Structure

```text
CodeAlpha_StockPortfolioTracker/
├── stock_portfolio_tracker.py
└── README.md
```

---

## 👤 Author

**Your Name**
Python Programming Intern at [CodeAlpha](https://www.codealpha.tech)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/YOUR_PROFILE)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?logo=github&logoColor=white)](https://github.com/YOUR_USERNAME)

<p align="center">
  ⭐ If you liked this project, give it a star! ⭐<br>
  Made with ❤️ during the <b>CodeAlpha</b> internship
</p>
