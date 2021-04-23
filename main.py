import sys

#Print the help menu
print('''
Calculator App
---------------
a -> Add/+
s -> Subtract/-
m -> Multiply/*
d -> Devide//
---------------
By CaspD3V
''')
#Number Variable
int1 = int(input("Number 1: "))
#Choose Addition, Subtraction, Multiplication, or Devision
choice = input("a, s, m, or d: ")
#Number Variable
int2 = int(input("Number 2: "))

#Making sure that the "choice" variable is always uppercase
if choice.upper() == "A":
    #Adding the 2 numbers together
    answer = int1 + int2
    #Printing out the math problem
    print(int1, "+", int2, "=", answer)
#Or subtracting
elif choice.upper() == "S":
    answer = int1 - int2
    print(int1, "-", int2, "=", answer)
#Or multiplying
elif choice.upper() == "M":
    answer = int1 * int2
    print(int1, "*", int2, "=", answer)
#Or deviding
elif choice.upper() == "D":
    answer = int1 / int2
    print(int1, "/", int2, "=", answer)
print("End")
#Exit the script
sys.exit()