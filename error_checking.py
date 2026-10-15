# Error Checking
# Jean de Klerk
# 16/10/26
# Version 1.4

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

'''def input_check(question): # 'question' is a placeholder
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
print(f"Your numbers added together result in {sum}")'''

# V1.4 Checking for valid input using try/except method
# Using parameters (placeholders) to make the code more puthonic
# FUnction that asks user to enter a number from a range
def valid_num(question, low, high):
    error = f"Whoops, that is not an integer between {low} and {high}."
    while True:
        try:
            response = int(input(question))
            # if the response >= to the low nr or <= high nr
            if low <= response <= high:
                break

            else:
                print(f"{error}\n")

        except ValueError:
            print(error)
    return response # This makes the response available to be used as a function

# Main Routine
if __name__ =="__main__":

    num1 = valid_num("Enter a number between 1-10: ", 1, 10)
    print(f"The number you enterered in {num1}. \n")

    num2 = valid_num("Enter a number between 15 and 20: ", 15, 20)
    print(f"The number you entered is {num2}.\n")

    num3 = valid_num("Enter a number between 80 and 100: ", 80, 100)
    print(f"The number you entered is {num3}.\n")

    #Multiply the resukt of num 1, num 2, and num 3
    multiply = num1 * num2 * num3
    print(f"The product of the mubers you entered is {multiply}")

    #Add the results of num 1, num2, num3
    sum = num1 + num2 +num3
    print(f"The sum of the three numbers you entered is {sum}")
    