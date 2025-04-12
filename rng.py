import random # imports the random command

gend = input("Ahoi! You a boy, girl or void? ").lower() # checks ur GENDAH

print(f"Good {gend}! Now input 2 numbers. :3") # heheehe

a = int(input("Your first number: ")) # takes input for the first number

b = int(input("Your second number: ")) # takes input for the second number

if a > b:   # compares the numbers to see if a is bigger than b, in that case it auto shuts down
    print(f"Bad {gend}! 3:") 
else:   # if the numbers are correct ur getting an output!
    print("Your silly number is: ", random.randint(a, b)) # prints the random number