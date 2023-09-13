class Bank:
    exchange_rate = 5000  # Default exchange rate: 5000 pesos per dollar

    def __init__(self, pesos):
        self.pesos = pesos
        self.dollars = self.pesos / Bank.exchange_rate

    def get_dollars(self):
        return self.dollars

# Create instances of the Bank class
account1 = Bank(15000)
account2 = Bank(25000)
account3 = Bank(35000)

# Print initial balances in dollars
print("Initial Balances in Dollars:")
print("Account 1:", account1.get_dollars())
print("Account 2:", account2.get_dollars())
print("Account 3:", account3.get_dollars())

# Update the exchange rate
Bank.exchange_rate = 5500  # New exchange rate: 5500 pesos per dollar

# Print updated balances in dollars
print("\nBalances in Dollars after Exchange Rate Update:")
print("Account 1:", account1.get_dollars())
print("Account 2:", account2.get_dollars())
print("Account 3:", account3.get_dollars())
