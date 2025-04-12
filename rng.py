import random

gend = input("Ahoi! You a boy, girl or void? ").lower()

print(f"Good {gend}! Now input 2 numbers. :3")

a = int(input("Your first number: "))

b = int(input("Your second number: "))

if a > b:
    print(f"Bad {gend}! 3:")
else:
    print("Your silly number is: ", random.randint(a, b))
