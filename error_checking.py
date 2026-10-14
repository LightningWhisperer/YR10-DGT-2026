# Error Checking
# Jean de Klerk
# 14/10/26
# Version 1

#Code that tests whether a valid input was give
'''done = True # Boolean variable set to True
while done:
    number_checker = int(input("Please enter your value as an integer: "))
    done = False

print(f"The number you entered is {number_checker}")'''

# Using a try and except method to check for valid input (V1.1)
# Use try and except method to catch errors

'''done = False
while not done:
    try: # This method tries for a valid input
        num = float(input("please enter a number: "))
        done = True

    except ValueError:
        print("That is not a valid float number. \nUse a fullstop as a decimal indicator.")

print(f"the number you entered is {num}")'''

# Checking for valid input and recycling code with a function (V1.2)
# for a number. A function is a chunck of code that does something
# Functions can be used over and over again
# To use a function (call it), write out its name with parnthesis at the end.
# To create a function, start with the word def

'''def input_check():
    while True:
        try:
            num = float(input("Please enter a number: "))
            break
        except ValueError:
            print("That is not a valid float number. \n")

    print(f"The number you entered us {num}")

# Main Routine
input_check() #This calls the funtion so that it can be used.'''

# V1.3 Valid input chekcer
# Use parameters in the function
# More Pythonic

def input_check(question): # 'question' is a placeholder
    while True:
        error = 'That is not a valid number'
        print(question)
        try:
            num = float(input())
            break
        except ValueError:
            print(error)

    return(num) #Gives back the value of num so that I can use it outside of the function

# Main routine
num1 = input_check("Please enter your first number:")
print(f"The number you stored is {num1}")

num2 = input_check("Please enter your second number:")
print(f"The second number you stored is {num2}")

sum = num1 + num2
print(f"Your numbers added together result in {sum}")

