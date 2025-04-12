import random

amber, ruby, esther = 0, 0, 0

gend = input("Ahoi! You a boy, girl or void? ").lower()
if gend == "":
    gend = "agender"
elif gend == "girl":
    print("Amber approves!")
    amber = 1
    
print(f"Good {gend}! Now input 2 numbers. :3")

a = int(input("Your first number: "))
if a == 42:
    print("Esther?!")
    esther = 1

b = int(input("Your second number: "))

if a > b:
    print(f"Bad {gend}! 3:")
elif a < b:
    print("Your silly number is: ", random.randint(a, b))
else:
    print("RUBYYYYYYYYYYYYYY!!!!")
    ruby = 1

if (ruby == 1 & esther == 1 & amber == 1):
    print("OMG OMG YOU COLLECTED ALL THE FAMILY! JADE WILL BE SO PROUD ///^///w///^///")
