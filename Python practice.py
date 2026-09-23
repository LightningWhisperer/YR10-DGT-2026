# this is a comment a # starts a comment
# Semester 2 Year 10DGT 2026 Demo code
# Author: Jean de Klerk
# Date: 16/09/2026
# Version:1

# Demonstration of how a while loop works
# and how indenting affects the code
'''keep_going = ""
while keep_going == "":
    print("Looping")
    print("Still looping")

    keep_going = input("Again")

print ("All Done")'''

#demonstrating error catching
'''keep_going = ""
while keep_going == "":
    try: 
            response = int(input("Number: "))
            print("You entered an interger.")

    except ValueError:
            print("Yikes! That is not an integer. Please try again")
keep_going = input("Do you want to keep going?")

print("All done thanks")'''


#functions
'''def greeting(name):# The 'name' is a placeholder
    print("Hello World! My name is", name)

greeting("Jean") # call the funtion to use it'''