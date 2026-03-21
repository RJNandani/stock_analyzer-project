# Stock Market Data Analyzer (NumPy Beginner Project)

Welcome to the **Stock Market Data Analyzer**! This is a beginner-level Python project designed to help you learn core data manipulation skills using `NumPy`.

## 📌 Project Overview
Instead of using complex libraries like `pandas`, this project challenges you to use pure `NumPy` to load, slice, and calculate statistics on tabular financial data. 

You will analyze a simulated 10-day dataset of a stock's price history (`stock_data.csv`).

## 🧠 NumPy Concepts Covered
1. **Loading Data**: Reading CSV files using `np.genfromtxt()`.
2. **Array Slicing**: Extracting 1D arrays (columns) from a 2D matrix (e.g., `data[:, 4]`).
3. **Descriptive Statistics**: Using `np.mean()`, `np.max()`, `np.min()`, and `np.std()`.
4. **Index Retrieval**: Using `np.argmax()` and `np.argmin()` to find the *index* of the highest or lowest value.
5. **Array Mathematics**: Subtracting and dividing arrays to calculate Daily Return percentages (`np.diff()`).
6. **Rolling Calculations**: Using `np.convolve()` to create a Simple Moving Average.

## 🚀 How to Run It

1. **Install NumPy** (if you haven't already):
   Open your terminal/command prompt and run:
   ```bash
   pip install numpy
   ```

2. **Run the Script**:
   Navigate to the project directory in your terminal and run:
   ```bash
   python stock_analyzer.py
   ```

## 🛠️ Next Steps / Challenges
Once you understand the code, try modifying it by:
- Adding more rows to `stock_data.csv` to see how the code handles 30 or 50 days of data.
- Calculating the "Daily Spread" (High Price minus Low Price) for each day using array subtraction.
- Changing the Simple Moving Average window from 3 days to 5 days.
