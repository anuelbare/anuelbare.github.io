print("Welcome to the tip calculator")
bill = int(input("How much was the total amount: N"))
tip = int(input("Choose how much tip you would like to give between 5, 10, 12 and 15: "))
people = int(input("How many people do you want to split the bill among: "))

tipPercent = tip/100
tipAmount = tipPercent * bill
currentBill = bill + tipAmount

results = round(currentBill/people, 2)
print(f"Each person should pay N{results}")