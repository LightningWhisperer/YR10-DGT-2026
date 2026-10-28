# 28/10/2026
# Jean de Klerk
# Fence cost calculator
# Version 1

# Error Checking
def num_check(question):

    # Error checking that a number is more than 0
    error_0 = "Please enter a number that is more than 0\n"
    # Error checking that a number is valid (not a word or roman numerals)
    error_message = "Please enter a valid number"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error_0)

        except ValueError:
            print(error_message)

# Main Routine
keep_going = ""
while keep_going == "":

    # Ask user for height and width
    length = num_check("Please enter the length of the fence: ")
    width = num_check("Please enter a the width of the fence: ")

    # Work out and display perimeter
    perimeter = 2 * (width + length)
    print()
    print(f"Perimeter: {perimeter} meters")

    # Ask user for $/m of fence
    cost = num_check("Please enter the price per meter of your fence: ")

    # Work out cost of the perimeter of the fence and display the cost of the fence
    cost_of_fence = perimeter * cost
 
    print(f"The cost of your fence is {cost_of_fence}")

    keep_going = input("Press enter to keep going or any key to quit  ")
    print()
    
    print("Thank you for using the area / perimeter calculator")
