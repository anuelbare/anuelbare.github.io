height = input("Please enter your height: ")

weight = input("Please enter your weight: ")
heightAsFloat = float(height)
weightAsInt = int(weight)

bmi = weightAsInt/(heightAsFloat**2)
print(round(bmi))
