# pyre-ignore-all-errors
import numpy as np
import os

def main():
    print("="*45)
    print("   STOCK MARKET DATA ANALYZER (NUMPY)   ")
    print("="*45)
    
    # 1. Load the data using NumPy
    # Columns in CSV: Day, Open, High, Low, Close, Volume
    # We use __file__ to ensure it finds the CSV in the exact same folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, 'stock_data.csv')
    
    print(f"\nLoading data from {filename}...\n")
    
    try:
        # np.genfromtxt is a great NumPy function for reading CSVs.
        # delimiter=',' splits columns by comma.
        # skip_header=1 ignores the first row (the text headers).
        data = np.genfromtxt(filename, delimiter=',', skip_header=1)
    except FileNotFoundError:
        print("Error: stock_data.csv not found! Please make sure the file is in the same directory.")
        return

    # 2. Extract columns into separate 1D NumPy arrays for easier operations
    # Syntax: data[:, index] means "give me all rows (:), and the column at 'index'"
    days = data[:, 0]
    open_prices = data[:, 1]
    high_prices = data[:, 2]
    low_prices = data[:, 3]
    close_prices = data[:, 4]
    volumes = data[:, 5]

    # 3. Calculate Basic Statistics on Closing Prices
    # NumPy has built-in functions for fast mathematical operations
    mean_close = np.mean(close_prices)
    max_close = np.max(close_prices)
    min_close = np.min(close_prices)
    # Standard deviation measures price volatility (how much it fluctuates)
    std_close = np.std(close_prices) 
    
    print("--- 📊 Basic Statistics (Closing Prices) ---")
    print(f"Average Closing Price:  ${mean_close:.2f}")
    print(f"Highest Closing Price:  ${max_close:.2f}")
    print(f"Lowest Closing Price:   ${min_close:.2f}")
    print(f"Price Volatility (Std): ${std_close:.2f}\n")

    # 4. Volume Analysis using Argmax
    # np.argmax returns the INDEX of the highest value in an array
    max_volume_idx = np.argmax(volumes)
    max_volume_day = days[max_volume_idx]
    print("--- 📈 Volume Analysis ---")
    print(f"Highest trading volume was {int(volumes[max_volume_idx])} on Day {int(max_volume_day)}.\n")

    # 5. Calculate Daily Returns (Percentage Change)
    # Formula: ((Today Close - Yesterday Close) / Yesterday Close) * 100
    # np.diff calculates the difference between consecutive elements (Array[n+1] - Array[n])
    daily_diff = np.diff(close_prices)
    
    # close_prices[:-1] gives us all prices EXCEPT the last one (these serve as the "Yesterday Close")
    daily_returns = (daily_diff / close_prices[:-1]) * 100
    
    # Analyze the daily returns
    best_day_idx = np.argmax(daily_returns)
    worst_day_idx = np.argmin(daily_returns)
    
    print("--- 🚀 Daily Returns Analysis ---")
    # Note: Because np.diff shortens the array by 1, index 0 in daily_returns corresponds to Day 2
    print(f"Best daily return:   {daily_returns[best_day_idx]:+.2f}% (on Day {int(days[best_day_idx + 1])})")
    print(f"Worst daily return:  {daily_returns[worst_day_idx]:+.2f}% (on Day {int(days[worst_day_idx + 1])})\n")

    # 6. Advanced Concept: Simple Moving Average (SMA) using Convolution
    # A moving average helps smooth out daily price spikes to view longer trends.
    window_size = 3
    if len(close_prices) >= window_size:
        # np.ones(3)/3 creates an array: [0.333, 0.333, 0.333]
        weights = np.ones(window_size) / window_size
        
        # np.convolve slides these weights across the prices to get the rolling average
        sma_3 = np.convolve(close_prices, weights, mode='valid')
        
        print("--- 📉 3-Day Simple Moving Average ---")
        for i, sma_val in enumerate(sma_3):
            print(f"Days {int(days[i])}-{int(days[i+window_size-1])} Average: ${sma_val:.2f}")

    # 7. Beginner Profit Calculator 💰
    # Uses simple math on the arrays we already have to simulate a real-world scenario
    shares = 100
    buy_price = close_prices[0]   # Price on the first day
    sell_price = close_prices[-1]  # Price on the last day
    
    total_investment = buy_price * shares
    final_value = sell_price * shares
    profit = final_value - total_investment
    
    # Calculate percentage return on investment (ROI)
    roi_percentage = (profit / total_investment) * 100
    
    print("\n--- 💰 Simple Profit Calculator ---")
    print(f"Simulating buying {shares} shares on Day {int(days[0])} and selling on Day {int(days[-1])}")
    print(f"Total Investment:   ${total_investment:.2f}")
    print(f"Final Value:        ${final_value:.2f}")
    
    if profit > 0:
        print(f"Total Profit:       +${profit:.2f} 🤑")
    else:
        print(f"Total Loss:         ${profit:.2f} 📉")
        
    print(f"Return on Invest.:  {roi_percentage:+.2f}%")
            
    print("\n" + "="*45)

if __name__ == "__main__":
    main()
