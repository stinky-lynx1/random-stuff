import random # imports the random command

amber, ruby, esther, terra = 0, 0, 0, 0

gend = input("Ahoi! You a boy, girl or void?\n").lower() 
if gend == "":
    gend = "agender"
elif gend == "girl":
    print("Amber approves!")
    amber = 1

print(f"Good {gend}! Now input 2 numbers. :3") # heheehe

a = int(input("Your first number:\n")) # takes input for the first number
if a == 42:
    print("Esther?!")
    esther = 1

b = int(input("Your second number:\n")) # takes input for the second number

if a > b:   # compares the numbers to see if a is bigger than b
    print(f"Bad {gend}! 3:") 
elif a < b:   # if the numbers are correct ur getting an output!
    print("Your silly number is:\n", random.randint(a, b)) # prints the random number
else:
    print("RUBYYYYYYYYYYYYYY!!!!")
    ruby = 1
    i = input()
    if i == "poof":
        terra = 1

if (ruby == 1 & esther == 1 & amber == 1 & terra == 1):
    print("OMG OMG YOU COLLECTED ALL THE FAMILY! JADE WILL BE SO PROUD ///^///w///^///")
