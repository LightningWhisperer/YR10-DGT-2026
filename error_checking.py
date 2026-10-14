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

done = False
while not done:
    try: # This method tries for a valid input
        num = float(input("please enter a number: "))
        done = True

    except ValueError:
        print("That is not a valid float number. \nUse a fullstop as a decimal indicator.")

print(f"the number you entered is {num}")
