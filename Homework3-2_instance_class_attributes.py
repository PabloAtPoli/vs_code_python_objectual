class Account:
    """This class represents a bank account that holds both dollars and pesos."""
    change = 5000 # value in pesos for 1 dollar

    def __init__(self, customer_name, balance_in_dollar=0, balance_in_pesos=0):
        self.customer_name = customer_name
        self.balance_in_dollar = balance_in_dollar
        self.balance_in_pesos = balance_in_pesos
    
    def deposit_money_in_pesos(self, amount_in_pesos):
        self.balance_in_pesos += amount_in_pesos
        self.balance_in_dollar = self.balance_in_pesos / Account.change     

    def withdraw_money_in_pesos(self, amount_in_pesos):
        self.balance_in_pesos -= amount_in_pesos
        self.balance_in_dollar = self.balance_in_pesos / Account.change
    
    def __str__(self):
        self.balance_in_dollar = self.balance_in_pesos / Account.change
        return f"Change: {Account.change}, Customer Name: {self.customer_name}, Balance in Pesos {self.balance_in_pesos}, Balance in Dollar: {self.balance_in_dollar}"
    

# Create instances of the Account class
a1 = Account("Alice")
a2 = Account("Herman")
a3 = Account("Pablo")

# Print account information
print("\nAccounts when they are created")
print(a1)
print(a2)
print(a3)

# Deposit money in pesos
a1.deposit_money_in_pesos(10000)
a2.deposit_money_in_pesos(20000)
a3.deposit_money_in_pesos(30000)

# Print account information after depositing money in pesos
print("\nAccounts after depositing money in pesos")
print(a1)
print(a2)
print(a3)

Account.change = 10000

a4 =  Account("Pedro")
a4.deposit_money_in_pesos(20000)

print("\nAccounts after changing the class attribute change")
print(a1)
print(a2)
print(a3)
print(a4)

# The output of the program shows that the class attribute change
# is shared by all instances of the Account class.
# When the value of the class attribute change is changed,
# the value of the instance attribute balance_in_dollar is also changed.
# This is because the value of the instance attribute balance_in_dollar
# is calculated from the value of the class attribute change.
