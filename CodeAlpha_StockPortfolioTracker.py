def stock_portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2800,
        "AMZN": 3500,
        "MSFT": 300
    }

    portfolio = {}

    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    while True:
        stock = input("\nEnter stock symbol to add (or type 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        elif stock not in stock_prices:
            print("Sorry, that stock is not in the list. Please enter a valid stock symbol.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock} shares: "))
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                continue
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue

        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

    # Calculate total investment
    total_investment = 0
    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        stock_value = stock_prices[stock] * qty
        total_investment += stock_value
        print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_value}")

    print(f"\nTotal Investment Value: ${total_investment}")

    # Optional: Save to a text file
    save = input("Would you like to save this portfolio to a file? (yes/no): ").lower()
    if save == "yes":
        filename = "portfolio.txt"
        with open(filename, "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("========================\n")
            for stock, qty in portfolio.items():
                stock_value = stock_prices[stock] * qty
                file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_value}\n")
            file.write(f"\nTotal Investment Value: ${total_investment}\n")
        print(f"Portfolio saved to {filename}")

if __name__ == "__main__":
    stock_portfolio_tracker()
