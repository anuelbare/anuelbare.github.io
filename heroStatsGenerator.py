import random

print('Welcome To The Hero Generator')
namae = input('What is your full name? ')

strength = random.randint(1, 20)
intelligence = random.randint(1, 20)
endurance = random.randint(1, 20)
stamina = random.randint(1, 20)
charisma = random.randint(1, 20)
total = strength + intelligence + endurance + stamina + charisma

if total >= 50:
    print(f'{namae} you have {strength} strength, {intelligence} intelligence, '
          f'{endurance} endurance, {stamina} stamina and {charisma} charisma. You will make a great hero.')
else:
    print(f'{namae} you have {strength} strength, {intelligence} intelligence, '
          f'{endurance} endurance, {stamina} stamina and {charisma} charisma. You are not fit to be  a hero')