# Creating a hot chocolate programme that a user will be able to interact with.
# Jean de Klerk
# 23/9/26
# Version 1

# TODO: record an input (store the answer)
#       check for valid answer (input checker)
#       Ask questions and respond

# Version 1
'''# Ask the user whether they like hot chocolate or not
like_hot_chocolate = input("Do you like hot chocolate? ")
print(like_hot_chocolate) #checking input is stored
print(f"Your answer was '{like_hot_chocolate}'.")

# Check the input and respond
if like_hot_chocolate == "Yes" or "y" or "yea" or "yeah" or "Y" or "Yea" or "Yeah" or "Of course" or "of course" or "yes":
    print("That is great! I like hot chocolate too.")
else:
    print("You are missing out! Why not give it a try?")'''

# Version 2
# While loop to test the programme
keep_going = ""
while keep_going == "":
    like_hot_chocolate = input("Do you like hot chocolate? ")
    # print(like_hot_chocolate) #checking input is stored
    print(f"Your answer was '{like_hot_chocolate}'.")

# Check the input and respond
    if like_hot_chocolate == "Yes" or like_hot_chocolate == "y" or like_hot_chocolate == "yea" or like_hot_chocolate == "yeah" or like_hot_chocolate == "Y" or like_hot_chocolate == "Yea" or like_hot_chocolate == "Yeah" or like_hot_chocolate == "Of course" or like_hot_chocolate == "of course" or like_hot_chocolate == "yes":
        print("That is great! I like hot chocolate too.")
        keep_going = "Finish"
    elif like_hot_chocolate == "No" or like_hot_chocolate == "no" or like_hot_chocolate == "N" or like_hot_chocolate == "n" or like_hot_chocolate == "nope":
        print("You are missing out! Why not give it a try?")
        keep_going = "akjdfghlakjdhg"
    else:
        print("I don't understand. Please try again.")