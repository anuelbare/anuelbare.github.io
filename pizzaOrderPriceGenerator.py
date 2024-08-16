print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15

    #checking for pepperoni
    if pepperoni == "Y":
        bill += 2
    elif pepperoni == "N":
        bill = bill

    #checking for cheese
    if extra_cheese == "Y":
        bill += 1
    elif extra_cheese == "N":
        bill = bill

if size == "M":
    bill = 20

    # checking for pepperoni
    if pepperoni == "Y":
        bill += 3
    elif pepperoni == "N":
        bill = bill

    # checking for cheese
    if extra_cheese == "Y":
        bill += 1
    elif extra_cheese == "N":
        bill = bill

if size == "L":
    bill = 25

    # checking for pepperoni
    if pepperoni == "Y":
        bill += 3
    elif pepperoni == "N":
        bill = bill

    # checking for cheese
    if extra_cheese == "Y":
        bill += 1
    elif extra_cheese == "N":
        bill = bill

else:
    print("Wrong Input)

print(f"Your final bill is ${bill}")
