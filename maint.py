from budget import Category 
from budget import create_spend_chart 

ledger1=Category("Food")
ledger2=Category("Clothing")
ledger3=Category("Auto")

print(ledger1)
print(ledger1.get_balance())
ledger1.deposit({"amount":1000,"description":""})
print(ledger1.get_balance())
ledger1.withdraw({"amount":445.87,"description":"Kupio bonbone"})
print(ledger1.ispis())

ledger1.transfer(100,ledger3)
print(ledger1.get_balance())
ledger1.transfer(188.88,ledger2)
ledger1.withdraw({"amount":105.87,"description":"Kupio vvvv"})
print(ledger1.get_balance())
ledger1.withdraw({"amount":10.87,"description":"Kupio vvvv"})
ledger1.transfer(8.88,ledger2)
ledger1.transfer(5.22,ledger2)
print(ledger1.get_balance())
print(ledger1.ispis())
print(ledger1.get_spend())

ledger2.deposit({"amount":400,"description":""})
ledger2.withdraw({"amount":445.87,"description":"Kupio bonbone"})
print(ledger2.get_balance())
print(ledger2.ispis())
print(ledger2.get_balance())
print(ledger2.get_spend())

ledger3.withdraw({"amount":10.17,"description":"Kupio hhhh"})
ledger3.deposit({"amount":770.77,"description":""})
ledger3.withdraw({"amount":310.17,"description":"Kupio tttt"})
print(ledger3.ispis())
print(ledger3.get_balance())
print(ledger3.get_spend())

ledger1.print()


	
p=create_spend_chart([ledger1,ledger2,ledger3])
print(p)
